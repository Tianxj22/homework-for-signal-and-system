#————————必做题—————————#
#——————分段阶跃信号——————#

import matplotlib.pyplot as plt
import numpy as np

def u_single(t):
    """单位阶跃信号"""
    if t < 0:
        return 0.
    elif t == 0:
        return 0.5
    return 1.

def u(t):
    """返回整个列表的阶跃信号"""
    ans = t.copy()
    n = len(t)
    for idx in range(n):
        ans[idx] = u_single(ans[idx])
    return ans

def fun(t):
    """函数为pi * sin(pi * t / 2) * (u(t) - u(t - 2))"""
    return np.pi * np.sin(np.pi * t / 2) * (u(t) - u(t - 2))

t = np.linspace(-1, 3, 10000)
ft = fun(t)

plt.plot(t, ft, linewidth=3)

# 设置图表标题，并给坐标轴加上标签
plt.title("pi * sin(pi * t / 2) * (u(t) - u(t - 2))", fontsize=24)
plt.xlabel("t", fontsize=14)
plt.ylabel("f(t)", fontsize=14)
plt.grid(True)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.savefig("/home/tianxj/myCode/homework/xinhaoyuxitong/1/graph/9.png")
plt.show()

# print(u_all([-3, -2, -1, 0, 1, 2, 3]))