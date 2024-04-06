#————————选做题—————————#
#——————sinc函数乘积信号——————#

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

def single_sinc(x):
    if abs(x) <= 1e-5:
        return 1
    return sin(x) / x

def sinc(x):
    ans = []
    for num in x:
        ans.append(single_sinc(num))
    return np.array(ans)

def fun(t):
    """函数为sinc(t) * sinc(t / 3) * sin(t / 5)"""
    return sinc(t) * sinc(t / 3) * sinc(t / 5)

t = np.linspace(-50, 50, 10000)
ft = fun(t)

plt.plot(t, ft, linewidth=3)

# 设置图表标题，并给坐标轴加上标签
plt.title("1000 * exp(-10^6t)", fontsize=24)
plt.xlabel("t/ms", fontsize=14)
plt.ylabel("U/V", fontsize=14)
plt.grid(True)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.savefig("/home/tianxj/myCode/homework/xinhaoyuxitong/1/graph/12.png")
plt.show()

# print(u_all([-3, -2, -1, 0, 1, 2, 3]))