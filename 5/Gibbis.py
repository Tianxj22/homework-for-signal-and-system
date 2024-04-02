#———————观察方波信号傅里叶分解时的Gibbis现象——————#

import matplotlib.pyplot as plt
import numpy as np
import os
from numpy import sin, pi, cos
from time import sleep

# 表示需要作图的是展开到第几项的图
n_show = [0, 1, 10, 100, 1000, 10000]

def square_fourier_param(n: int) -> float:
    '''返还方波周期信号的傅里叶级数
        这里的方波信号设为周期为2, 占空比50%, 幅值为1'''
    if not n:
        return 0.5
    return 2 * sin(n * pi / 2) / (n * pi)

def trangle_fourier_param(n: int) -> float:
    '''返还锯齿波周期信号的傅里叶级数
    '''
    if not n:
        return 0.5
    return -2 * cos(n * pi) / (n * pi)

def square_fourier(t, n: int):
    '''返回方波信号的第n项傅里叶级数式
       这里的方波信号设为周期为2, 占空比50%, 幅值为1'''
    an = square_fourier_param(n)
    return an * cos(n * pi * t)

def trangle_fourier(t, n: int):
    '''返回锯齿波信号的第n项傅里叶级数式
    '''
    bn = trangle_fourier_param(n)
    return bn * sin(n * pi * t)

# 获取源码所在路径
fileroot = os.path.dirname(os.path.realpath(__file__))

x_value = np.linspace(-5, 5, 100000)
y1_value = np.array([0. for _ in x_value])
y2_value = np.array([0. for _ in x_value])

for n in range(0, 10001):
    y1_value += square_fourier(x_value, n)
    y2_value += trangle_fourier(x_value, n)

    if not n_show.count(n):
        continue

    plt.plot(x_value, y1_value, label='square', linewidth = 1)
    plt.plot(x_value, y2_value, label="trangle", linewidth = 1)

    # 设置图表标题并给坐标轴加上标签
    plt.title(f"{n} fourier", fontsize=24)
    plt.xlabel("t", fontsize=14)
    plt.ylabel("f(t)", fontsize=14)
    plt.legend()

    # 设置刻度标记的大小
    plt.tick_params(axis='both', which='major', labelsize=14)

    plt.savefig(f"{fileroot}/graph/{n}_fourier.jpg")
    plt.show()