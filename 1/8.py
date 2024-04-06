#————————必做题—————————#
#——————分段阶跃信号——————#

import matplotlib.pyplot as plt
import numpy as np

def u(t):
    """单位阶跃信号"""
    if t < 0:
        return 0.
    elif t == 0:
        return 0.5
    return 1.

def u_all(t):
    """返回整个列表的阶跃信号"""
    ans = t.copy()
    n = len(t)
    for idx in range(n):
        ans[idx] = u(ans[idx])
    return ans

# def fun(t):
#     """函数为e^-0.25t * u(t)"""
#     return np.exp(-0.25 * t) * u_all(t.copy())

t = np.linspace(-2, 2, 10000)
ft = 0.8 + 1.2 * u_all(t) - 1.6 * u_all(t - 1) + 2.1 * u_all(t - 1.8)

plt.plot(t, ft, linewidth=3)

# 设置图表标题，并给坐标轴加上标签
plt.title("f(t + 2) - 3f(t) + 2f(t - 1)", fontsize=24)
plt.xlabel("t", fontsize=14)
plt.ylabel("f(t)", fontsize=14)
plt.grid(True)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.savefig("/home/tianxj/myCode/homework/xinhaoyuxitong/1/graph/8.png")
plt.show()

# print(u_all([-3, -2, -1, 0, 1, 2, 3]))