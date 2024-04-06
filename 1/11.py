#————————选做题—————————#
#——————电感放电信号波形——————#

import matplotlib.pyplot as plt
import numpy as np
from numpy import *

# def u_single(t):
#     """单位阶跃信号"""
#     if t < 0:
#         return 0.
#     elif t == 0:
#         return 0.5
#     return 1.

# def u(t):
#     """返回整个列表的阶跃信号"""
#     ans = t.copy()
#     n = len(t)
#     for idx in range(n):
#         ans[idx] = u_single(ans[idx])
#     return ans

def fun(t):
    """函数为1000 * exp(-10^6t)"""
    return 1000 * exp(-1000 * t)

t = np.linspace(0, 0.01, 10000)
ft = fun(t)

plt.plot(t, ft, linewidth=3)

# 设置图表标题，并给坐标轴加上标签
plt.title("1000 * exp(-10^6t)", fontsize=24)
plt.xlabel("t/ms", fontsize=14)
plt.ylabel("U/V", fontsize=14)
plt.grid(True)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.savefig("/home/tianxj/myCode/homework/xinhaoyuxitong/1/graph/11.png")
plt.show()

# print(u_all([-3, -2, -1, 0, 1, 2, 3]))