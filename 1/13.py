#————————选做题—————————#
#——————双边sinc函数序列——————#

import matplotlib.pyplot as plt
import numpy as np
from numpy import *

def fun(t):
    """函数为f[n] = sin(0.1 pi n) / 0.1 pi n"""
    ans = []
    for n in t:
        if abs(n) < 1e-5:
            ans.append(1)
        else:
            ans.append(sin(0.1 * pi * n) / (0.1 * pi * n))
    return np.array(ans)

lb = -50
ub = 50
x_value = np.linspace(lb, ub, ub - lb + 1, endpoint=True)
y_value = fun(x_value)

t = np.linspace(lb, ub, 10000)

plt.stem(x_value, y_value, label="f(n)")
# plt.plot(t, np.cos(np.pi * t ** 2 / 3), dashes=[6,2], linewidth=1, label="u_b")
# plt.plot(t, np.cos(np.pi * t ** 2 / 3), dashes=[6,2], linewidth=1, label="l_b")

# 设置图表标题，并给坐标轴加上标签
plt.title("sin(0.1 pi n) / 0.1 pi n", fontsize=24)
plt.xlabel("t", fontsize=14)
plt.ylabel("f(t)", fontsize=14)
plt.grid(True)
plt.legend(loc='upper right')

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.savefig("/home/tianxj/myCode/homework/xinhaoyuxitong/1/graph/13.png")
plt.show()

# print(u_all([-3, -2, -1, 0, 1, 2, 3]))