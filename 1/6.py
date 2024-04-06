#————————必做题—————————#
#——————奇怪的周期序列——————#

import matplotlib.pyplot as plt
import numpy as np

def fun(n):
    """函数为f[n] = cos[pi * n ^ 2 / 3]"""
    return np.cos(np.pi * n ** 2 / 3)

lb = -10
ub = 10
x_value = np.linspace(lb, ub, ub - lb + 1, endpoint=True)
y_value = fun(x_value)

t = np.linspace(lb, ub, 10000)

plt.stem(x_value, y_value, label="f(n)")
plt.plot(t, np.cos(np.pi * t ** 2 / 3), dashes=[6,2], linewidth=1, label="u_b")
plt.plot(t, np.cos(np.pi * t ** 2 / 3), dashes=[6,2], linewidth=1, label="l_b")

# 设置图表标题，并给坐标轴加上标签
plt.title("cos[pi * n ^ 2 / 3]", fontsize=24)
plt.xlabel("t", fontsize=14)
plt.ylabel("f(t)", fontsize=14)
plt.grid(True)
plt.legend(loc='upper right')

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.savefig("/home/tianxj/myCode/homework/xinhaoyuxitong/1/graph/6.png")
plt.show()

# print(u_all([-3, -2, -1, 0, 1, 2, 3]))