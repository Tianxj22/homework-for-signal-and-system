#——————Dirichlet条件————————#

import matplotlib.pyplot as plt
import numpy as np
import os
from numpy import sin, pi, cos
from time import sleep

# 表示需要作图的是展开到第几项的图
n_show = [0, 1, 10, 100, 1000, 10000]

#——————————————————————————————————————————————————
def f_x(x_values):
    '''阶跃'''
    ans = []
    for x in x_values:
        if x > -2.5 and x < 2.5:
            ans.append(1)
        else:
            ans.append(0)
    return np.array(ans)

def setfv(t):
    tn = len(t)
    f = np.zeros(tn)
    for i in range(20):
        v = 2**(-i)
        startn = int(tn - v*tn)
        f[startn:] = v
    return f
#————————————————————————————————————————————————————


# 获取源码所在路径
fileroot = os.path.dirname(os.path.realpath(__file__))

x_value = np.linspace(0, 1, 10000)
y_value = setfv(x_value)

# 计算傅里叶变换系数
F_f_x = np.fft.fft(y_value)
real_part = F_f_x.real
imgrant_part = F_f_x.imag
print(len(F_f_x))

# 获取频域的横坐标
n = x_value.size
timestep = x_value[1] - x_value[0]  # 采样间隔
freq = np.fft.fftfreq(n, d=timestep)
# print(freq)

plt.plot(x_value, y_value, label='square', linewidth = 1)

# 设置图表标题并给坐标轴加上标签
plt.title("f(t)", fontsize=24)
plt.xlabel("t", fontsize=14)
plt.ylabel("f(t)", fontsize=14)
plt.legend()

    # 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

# plt.show()

m = 1
# 下面用正弦信号模拟
for i in range(2000):
    startm = m * (i+1)
    dataf = np.fft.fft(y_value)
    dataf[startm:-startm] = 0

    if not n_show.count(i):
        continue

    plt.clf()
    plt.plot(x_value, np.real(np.fft.ifft(dataf)), label='simulate')
    plt.plot(x_value, y_value, label='origin')
    plt.xlabel("t")
    plt.ylabel("ifft(data)")
    plt.grid(True)
    plt.title(f'n = {i}')
    plt.legend()
    plt.show()
