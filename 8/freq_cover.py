#——————————————————————————————————————频率混叠——————————————————————————————————————————————————#

#————————————————————————————————————————头文件——————————————————————————————————————————————————#

import os
import numpy as np
import matplotlib.pyplot as plt
from numpy import exp, sin, cos, pi

#————————————————————————————————————————常量————————————————————————————————————————————————————#

cur_dir = os.path.dirname(os.path.realpath(__file__))
save_dir = os.path.join(cur_dir, 'pic')

fs = 1000  # 采样频率
t = np.linspace(0, 5, fs)  # 时间向量
f_carrier = 0.5  # 载波频率

#————————————————————————————————————————函数———————————————————————————————————————————————————#



#——————————————————————————————————————程序主体——————————————————————————————————————————————————#

base = exp(-(t - 2.5) ** 2 / 1.5)
# carrier = base * 0.5 * cos(2 * pi * 0.5 * t)
# plt.subplot(1, 2, 1)
# plt.plot(t, carrier, label='carrier')
# plt.plot(t, base, label='base')
# plt.title('ft')
# plt.grid(True)
# plt.legend()

# n = len(base)
# freq = np.fft.fftfreq(n, d=1/fs)
# fft_vals1 = np.fft.fft(base)
# magnitude1 = np.abs(fft_vals1)

# fft_vals2 = np.fft.fft(carrier)
# magnitude2 = np.abs(fft_vals2)

# plt.subplot(1, 2, 2)
# plt.plot(freq, magnitude1, label='base_Fw')
# plt.plot(freq, magnitude2, label='carrier_Fw')
# plt.title('Fw')
# plt.grid(True)
# plt.legend()
# plt.show()

carrier_real = base * 0.5 * cos(2 * pi * f_carrier * t)
carrier_imag = base * 0.5 * sin(2 * pi * f_carrier * t)

plt.plot(t, carrier_real, label='carrier_real')
plt.plot(t, carrier_imag, label='carrier_imag')
plt.plot(t, carrier_real * 0.5 * cos(2 * pi * f_carrier * t), label='carrier_real * cos')
plt.plot(t, carrier_imag * 0.5 * sin(2 * pi * f_carrier * t), label='carrier_imag * sin')
plt.plot(t, carrier_real * 0.5 * cos(2 * pi * f_carrier * t) + 
         carrier_imag * 0.5 * sin(2 * pi * f_carrier * t), label='recovery')
plt.grid(True)
plt.legend()
plt.savefig(os.path.join(save_dir, 'recovery.png'))
plt.show()