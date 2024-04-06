#————————必做题—————————#
#——————分段阶跃信号——————#

import matplotlib.pyplot as plt
import numpy as np
from numpy import *

def fun(t):
    """函数为exp(-(t / 2) ** 2) * cos(pi * t)"""
    return exp(-1 * (t / 2) ** 2) * cos(pi * t)

t = np.linspace(-5, 5, 10000)
ft = fun(t)

plt.plot(t, ft, linewidth=3)
plt.plot(t, exp(- (t / 2) ** 2), dashes=[6,2], linewidth=1, label="u_b")
plt.plot(t, -exp(- (t / 2) ** 2), dashes=[6,2], linewidth=1, label="l_b")
plt.plot(t, cos(pi * t), dashes=[6,2], linewidth=1, label="cos")

# 设置图表标题，并给坐标轴加上标签
plt.title("pi * sin(pi * t / 2) * (u(t) - u(t - 2))", fontsize=24)
plt.xlabel("t", fontsize=14)
plt.ylabel("f(t)", fontsize=14)
plt.grid(True)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.savefig("/home/tianxj/myCode/homework/xinhaoyuxitong/1/graph/10.png")
plt.show()

# print(u_all([-3, -2, -1, 0, 1, 2, 3]))