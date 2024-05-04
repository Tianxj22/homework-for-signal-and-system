#——————————————————————————————单边带信号模拟——————————————————————————————#


#—————————————————————————————————头文件——————————————————————————————————#

import os
import matplotlib.pyplot as plt
from random import *
import numpy as np
from numpy import pi, cos, sin, where
from scipy.fftpack import hilbert

#——————————————————————————————————常量——————————————————————————————————#

# 码流的大小
bite_num = 50
# 1bite数据传输的时间
during_sec = 5
# 调制的频率
fc = 2700
wc = 2 * pi * fc

cur_dir = os.path.dirname(os.path.realpath(__file__))
save_dir = os.path.join(cur_dir, 'pic')

#——————————————————————————————————函数——————————————————————————————————#

def four_encoding(bite_string: list):
    '''对码流进行四电平编码'''
    rt = []
    for idx in range(0, int(len(bite_string)), 2):
        try:
            rt.append(bite_string[idx] * 4 + bite_string[idx + 1] * 2 - 3)
        except:
            rt.append(bite_string[idx] * 4 - 3)
    return rt

def upper_cos(t, A: float,  t0: float, w: float):
    '''返回升余弦信号(1 + Acos(w(t - t0))) / 2
        t0: 升余弦的中心点
        w: 频率
        注意 该频率只会绘制-pi 到 pi'''
    rt = []
    for ti in t:
        if -pi < w * (ti - t0) and w * (ti - t0) < pi:
            rt.append(A * (1 + cos(w * (ti - t0))) / 2)
        else:
            rt.append(0.)
    return rt
    
def draw_and_save(t, ft, save = True, save_name = ""):
    '''绘制并保存'''
    plt.plot(t, ft)
    plt.grid(True)
    if save:
        plt.savefig(os.path.join(save_dir, f'{save_name}.png'))
    plt.close()

def draw_Fw(f, fs, title="Frequency Spectrum"):
    '''绘制给定信号的幅度频谱'''
    n = len(f)
    freq = np.fft.fftfreq(n, d=1/fs)  # 计算频率轴
    ft = np.fft.fft(f)
    magnitude = np.abs(ft)  # 计算FFT的幅值
    
    # 绘制幅度频谱
    plt.plot(freq[:n // 2], magnitude[:n // 2], label=title)  # 只绘制正频率部分
    # plt.title(title)
    # plt.xlabel("Frequency (Hz)")
    # plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True)
    # plt.show()


#——————————————————————————————————主体——————————————————————————————————#

# 生成码流
bite_string = [randint(0, 1) for _ in range(bite_num)]

# 绘制码流图
t = np.linspace(0, during_sec * bite_num, bite_num * 100)
y = [bite_string[int(ti / during_sec) - 1] for ti in t]
draw_and_save(t, y, True, save_name='bite_string')

fe_string = four_encoding(bite_string)
print(fe_string)

# 绘制四电平编码后的码流
t = np.linspace(0, (during_sec * bite_num * 0.5), bite_num * 100)
y = [fe_string[int(ti / during_sec)] for ti in t[0: -1]]
y.append(fe_string[-1])
draw_and_save(t, y, save_name='four_encoding')

# 绘制升余弦信号
t = np.linspace(-2 * pi, 2 * pi, 1000)
y = upper_cos(t, 3, 0, pi / 2)
draw_and_save(t, y, save_name='upper_cos')

# 进行升余弦脉冲编码
t = np.linspace(0.1, (during_sec * (bite_num + 2) * 0.5), bite_num * 100)
uc_encoding = np.zeros(np.shape(t), np.float32)
for idx in range(len(fe_string)):
    uc_encoding += upper_cos(t, fe_string[idx], (idx + 1) * during_sec, pi / during_sec)
draw_and_save(t, uc_encoding, save_name='upper_cos_encoding')

# 希尔伯特变换
hbt = hilbert(uc_encoding.copy())
draw_and_save(t, hbt, save_name='hbt')

# plt.plot(t, uc_encoding, label='uc')
# plt.plot(t, hbt, label='hbt')
# plt.legend()
# plt.show()

# 移相法调制
out1 = uc_encoding * cos(wc * t)
out2 = hbt * sin(wc *t)
final_out = out1 - out2

draw_and_save(t, final_out, save_name='final_out')


# plt.subplot(1, 3, 1)
draw_Fw(uc_encoding, 2 * during_sec, 'uc_encode')
# plt.subplot(1, 3, 2)
draw_Fw(final_out, 2 * during_sec, 'final_out')
# plt.subplot(1, 3, 3)
draw_Fw(cos(wc * t), 2 * during_sec, 'carryer')
plt.savefig(os.path.join(save_dir, '输出频谱比较图.png'))