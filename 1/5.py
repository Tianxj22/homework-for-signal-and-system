#————————必做题—————————#
#——————衰减震荡序列——————#

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

def fun(n):
    """函数为f[n] = cos(0.1 * pi * n) * exp(-n / 15) * u[n]"""
    return np.cos(0.1 * np.pi * n) * np.exp(- n / 15) * u_all(n.copy())

lb = -30
ub = 30
x_value = np.linspace(lb, ub, ub - lb + 1, endpoint=True)
y_value = fun(x_value)

t = np.linspace(lb, ub, 10000)

plt.stem(x_value, y_value, label="f(n)")
plt.plot(t, np.exp(-t / 15) * u_all(t.copy()), dashes=[6,2], linewidth=1, label="u_b")
plt.plot(t, -np.exp(-t / 15) * u_all(t.copy()), dashes=[6,2], linewidth=1, label="l_b")

# 设置图表标题，并给坐标轴加上标签
plt.title("cos(0.1 * pi * n) * exp(-n / 15) * u[n]", fontsize=24)
plt.xlabel("t", fontsize=14)
plt.ylabel("f(t)", fontsize=14)
plt.grid(True)
plt.legend(loc='upper right')

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.savefig("/home/tianxj/myCode/homework/xinhaoyuxitong/1/graph/5.png")
plt.show()

# print(u_all([-3, -2, -1, 0, 1, 2, 3]))