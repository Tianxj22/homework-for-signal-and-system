#————————选做题—————————#
#——————具有无限多个极大值极小值的有限长信号——————#

import matplotlib.pyplot as plt
import numpy as np
from numpy import *

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

# def single_sin_t(x):
#     if abs(x) <= 1e-5:
#         return 0
#     return sin(2 * pi / t)

# def sin_t(x):
#     ans = []
#     for num in x:
#         ans.append(single_sin_t(num))
#     return np.array(ans)

def fun(t):
    """函数为sin(2 * pi / t) * u(t)"""
    return sin(2 * pi / t) * u(t)

t = np.linspace(-10, 10, 1000000)
ft = fun(t)

plt.plot(t, ft, linewidth=1)

# 设置图表标题，并给坐标轴加上标签
plt.title("sin(2 * pi / t) * u(t)", fontsize=24)
plt.xlabel("t", fontsize=14)
plt.ylabel("f(t)", fontsize=14)
plt.grid(True)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.savefig("/home/tianxj/myCode/homework/xinhaoyuxitong/1/graph/14.png")
plt.show()

# print(u_all([-3, -2, -1, 0, 1, 2, 3]))