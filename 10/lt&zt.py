#————————————————————————————————————————————进行Laplace变换————————————————————————————————————————————————#
#———————————————————————————————————————————————头文件——————————————————————————————————————————————————————#

from sympy import symbols, laplace_transform, exp, inverse_laplace_transform, Heaviside

#————————————————————————————————————————————————常量——————————————————————————————————————————————————————#



#————————————————————————————————————————————————函数——————————————————————————————————————————————————————#



#——————————————————————————————————————————————程序主体————————————————————————————————————————————————————#

# 定义符号
t, s = symbols('t s')

# 定义函数
f = exp(-3 * t) * Heaviside(t)

# 计算Laplace变换
F_s = laplace_transform(f, t, s)

# 输出结果
print(F_s)


# 定义符号
t, s = symbols('t s')

# 定义拉普拉斯变换后的函数
F_s = 1 / ((s + 1) * (s + 2))

# 计算拉普拉斯反变换
f_t = inverse_laplace_transform(F_s, s, t)

# 输出结果
print(f_t)

import sympy as sp

def z_transform(f, n, z):
    F = sp.Sum(f * z**(-n), (n, 0, sp.oo))
    return sp.simplify(F.doit())

# 定义符号
n, z = sp.symbols('n z')

# 定义时间域的序列
f_n = 2**n

# 计算 Z 变换
F_z = z_transform(f_n, n, z)

# 输出结果
print(F_z)


import sympy as sp

def inverse_z_transform(F, z, n):
    # 分解为部分分式
    F_partial = sp.apart(F, z)
    f_n = 0
    
    # 对每一个部分分式计算其对应的时间序列
    for term in F_partial.as_ordered_terms():
        # 如果是常数项
        if term.is_constant():
            f_n += term * sp.DiracDelta(n)
        else:
            # 提取分子的系数和分母的根
            num, den = term.as_numer_denom()
            root = sp.roots(den, z)
            for r, mult in root.items():
                f_n += num.subs(z, r) * (r**n) / sp.factorial(n)
    
    return sp.simplify(f_n)

# 定义符号
n, z = sp.symbols('n z')

# 定义 Z 域的函数
F_z = z / (z - 2)

# 计算逆 Z 变换
f_n = inverse_z_transform(F_z, z, n)

# 输出结果
print(f_n)
