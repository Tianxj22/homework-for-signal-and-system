import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert
from numpy import exp, cos, pi

# 参数设置
fs = 1000  # 采样频率
t = np.linspace(0, 5, fs)  # 时间向量
f_base = 10  # 基带信号频率
f_carrier = 100  # 载波频率

# 生成基带信号
# base_signal = np.cos(2 * np.pi * f_base * t)

base = exp(-(t - 2.5) ** 2 / 1.5)
carrier = base * 0.5 * cos(2 * pi * 0.5 * t)

plt.subplot(1, 2, 1)
plt.plot(t, carrier, label='carrier')
plt.plot(t, base, label='base')
plt.title('ft')
plt.grid(True)
plt.legend()

n = len(base)
freq = np.fft.fftfreq(n, d=1/fs)
fft_vals1 = np.fft.fft(base)
magnitude1 = np.abs(fft_vals1)

fft_vals2 = np.fft.fft(carrier)
magnitude2 = np.abs(fft_vals2)

plt.subplot(1, 2, 2)
plt.plot(freq, magnitude1, label='base_Fw')
plt.plot(freq, magnitude2, label='carrier_Fw')
plt.title('Fw')
plt.grid(True)
plt.legend()
plt.show()


# 希尔伯特变换生成解析信号
# analytic_signal = hilbert(base_signal)

# # 生成载波
# carrier = np.cos(2 * np.pi * f_carrier * t)
# carrier_quadrature = np.sin(2 * np.pi * f_carrier * t)

# # SSB调制 (上边带)
# ssb_signal = np.real(analytic_signal) * carrier - np.imag(analytic_signal) * carrier_quadrature

# # 计算FFT并绘制结果
# n = len(ssb_signal)
# freq = np.fft.fftfreq(n, d=1/fs)
# fft_vals = np.fft.fft(ssb_signal)
# magnitude = np.abs(fft_vals)

# 绘制幅度频谱图
# plt.figure(figsize=(10, 5))
# plt.plot(freq[:n // 2], magnitude[:n // 2])  # 只显示正频率部分
# plt.axvline(x=f_carrier, color='red', linestyle='--', label='Carrier Frequency')  # 标记载波频率
# plt.title("Frequency Spectrum of the SSB Signal")
# plt.xlabel("Frequency (Hz)")
# plt.ylabel("Magnitude")
# plt.legend()
# plt.grid(True)
# plt.show()