#————————必做题—————————#
#——————三角信号——————#

import matplotlib.pyplot as plt
import numpy as np

def f(t):
    """单位斜变信号"""
    if t < 0:
        return 0.
    return t

def f_all(t):
    """返回整个列表的阶跃信号"""
    ans = t.copy()
    n = len(t)
    for idx in range(n):
        ans[idx] = f(ans[idx])
    return ans

# def fun(t):
#     """函数为e^-0.25t * u(t)"""
#     return np.exp(-0.25 * t) * u_all(t.copy())

x_value = np.linspace(-2, 2, 10000)
y_value = f_all(x_value + 2) - 3 * f_all(x_value) + 2 * f_all(x_value - 1)

plt.plot(x_value, y_value, linewidth=3)

# 设置图表标题，并给坐标轴加上标签
plt.title("f(t + 2) - 3f(t) + 2f(t - 1)", fontsize=24)
plt.xlabel("t", fontsize=14)
plt.ylabel("f(t)", fontsize=14)
plt.grid(True)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.savefig("/home/tianxj/myCode/homework/xinhaoyuxitong/1/graph/7.png")
plt.show()

# print(u_all([-3, -2, -1, 0, 1, 2, 3]))