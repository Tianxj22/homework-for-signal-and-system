#————————必做题—————————#
#——————单边指数信号——————#

import matplotlib.pyplot as plt
import numpy as np

def u(t):
    """单位阶跃信号"""
    if t > 0:
        return 1.
    elif t < 0:
        return 0.
    return 0.5

def u_all(t):
    """返回整个列表的阶跃信号"""
    n = len(t)
    for idx in range(n):
        t[idx] = u(t[idx])
    return t

def fun(t):
    """函数为e^-0.25t * u(t)"""
    return np.exp(-0.25 * t) * u_all(t.copy())

x_value = np.linspace(-30, 30, 10000)
y_value = fun(x_value)

plt.plot(x_value, y_value, linewidth=3)

# 设置图表标题，并给坐标轴加上标签
plt.title("exp(-0.25t)u(t)", fontsize=24)
plt.xlabel("t", fontsize=14)
plt.ylabel("f(t)", fontsize=14)
plt.grid(True)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.savefig("/home/tianxj/myCode/homework/xinhaoyuxitong/1/graph/1.png")
plt.show()

# print(u_all([-3, -2, -1, 0, 1, 2, 3]))