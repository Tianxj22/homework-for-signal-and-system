#————————必做题—————————#
#——————右边指数衰减震荡信号——————#

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
    """函数为exp(-0.1t) * cos(pi * t) * u(t)"""
    return np.exp(-0.1 * t) * np.cos(np.pi * t) * u_all(t.copy())

def upper_bound(t):
    """信号的上界"""
    return np.exp(-0.1 * t) * u_all(t.copy())

def lower_bound(t):
    """信号的下界"""
    return -np.exp(-0.1 * t) * u_all(t.copy())

x_value = np.linspace(-30, 30, 10000)
y_value = fun(x_value)
l_b = lower_bound(x_value)
u_b = upper_bound(x_value)

plt.plot(x_value, y_value, linewidth=1, label="f(t)")
plt.plot(x_value, l_b, dashes=[6,2], linewidth=1, label="l_b")
plt.plot(x_value, u_b, dashes=[6,2], linewidth=1, label="u_b")

# 设置图表标题，并给坐标轴加上标签
plt.title("exp(-0.1t) * cos(pi * t) * u(t)", fontsize=24)
plt.xlabel("t", fontsize=14)
plt.ylabel("f(t)", fontsize=14)
plt.grid(True)
plt.legend(loc='upper right')

# 设置刻度标记的大小
# plt.tick_params(axis='both', labelsize=24)

plt.savefig("/home/tianxj/myCode/homework/xinhaoyuxitong/1/graph/3.png")
plt.show()

# print(u_all([-3, -2, -1, 0, 1, 2, 3]))