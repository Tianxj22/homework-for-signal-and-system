#————————求解信号的傅里叶变换——————————#

#—————————————头文件————————————————#

import numpy as np
import matplotlib.pyplot as plt
from numpy import exp, heaviside
import os

#———————————————函数————————————————#

def f1(t):
    '''f(t) = t'''
    return t

def f2(t):
    '''exp(-t ** 2)'''
    return exp(-t ** 2)

def f3(t):
    '''exp(-t) * heaviside(t, 0.5)'''
    return exp(-t) * heaviside(t, 0.5)

def f4(t):
    '''heaviside(t + 1, 0.) + heaviside(t - 1, 0.)'''
    return heaviside(t + 1, 0.) - heaviside(t - 1, 0.)

def f5(t):
    '''(heaviside(t + 1, 0.) - heaviside(t - 1, 0.)) * (1 - abs(t))'''
    return (heaviside(t + 1, 0.) - heaviside(t - 1, 0.)) * (1 - abs(t))

def F1(w):
    '''w * exp(-3 * w) * heaviside(w, 0.)'''
    return w * exp(-3 * w) * heaviside(w, 0.)

def F2(w):
    '''1 / (1 + w ** 2)'''
    return 1 / (1 + w ** 2)

def F3(w):
    '''w'''
    return w

def F4(w):
    '''heaviside(w + 1) - heaviside(w - 1)'''
    return heaviside(w + 1, 0.) - heaviside(w - 1, 0.)

#——————————————程序主体——————————————#

# 获取存储路径
program_root = os.path.dirname(os.path.realpath(__file__))
save_root = os.path.join(program_root, 'graph')

t_values = np.linspace(-2, 2, 1000)
f1_values = f1(t_values)
f2_values = f2(t_values)
f3_values = f3(t_values)
f4_values = f4(t_values)
f5_values = f5(t_values)


plt.plot(t_values, f1(t_values), label='f1(t)')
plt.plot(t_values, f2(t_values), label='f2(t)')
plt.plot(t_values, f3(t_values), label='f3(t)')
plt.plot(t_values, f4(t_values), label='f4(t)')
plt.plot(t_values, f5(t_values), label='f5(t)')
plt.title("functions")
plt.xlabel('t', fontsize=10)
plt.ylabel('f(t)', fontsize=12)
plt.legend()

plt.savefig(f"{save_root}/f(t).jpg")
plt.show()


# 频域图像
w_values = np.linspace(-2, 2, 1000)

F1_values = F1(w_values)
F2_values = F2(w_values)
F3_values = F3(w_values)
F4_values = F4(w_values)

plt.plot(w_values, F1_values, label='F1(t)')
plt.plot(w_values, F2_values, label='F2(t)')
plt.plot(w_values, F3_values, label='F3(t)')
plt.plot(w_values, F4_values, label='F4(t)')
plt.title("Functions")
plt.xlabel('w', fontsize=10)
plt.ylabel('F(w)', fontsize=12)
plt.legend()

plt.savefig(f"{save_root}/F(w).jpg")
plt.show()