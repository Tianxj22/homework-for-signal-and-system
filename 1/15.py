#————————选做题—————————#
#——————波形发散的周期信号——————#

import matplotlib.pyplot as plt
import numpy as np
from numpy import *

x = linspace(0.1, 1, 100)

for i in range(-3, 3):
    t = x + i
    plt.plot(t, 1 / x, 'b-', linewidth = 1)
    tn = [i, i]
    yn = [-0.5, 10]
    plt.plot(tn, yn, 'y--', linewidth = 1)

# 设置图表标题，并给坐标轴加上标签
plt.title("sin(0.1 pi n) / 0.1 pi n", fontsize=24)
plt.xlabel("t", fontsize=14)
plt.ylabel("f(t)", fontsize=14)
plt.grid(True)
plt.legend(loc='upper right')

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.savefig("/home/tianxj/myCode/homework/xinhaoyuxitong/1/graph/15.png")
plt.show()

# print(u_all([-3, -2, -1, 0, 1, 2, 3]))