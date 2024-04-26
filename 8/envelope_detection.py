#——————————————————————包络线检测制图———————————————————————#

#—————————————————————————头文件——————————————————————————#

import os
import matplotlib.pyplot as plt
import numpy as np
from numpy import sin, cos, pi
from scipy.signal import argrelextrema

#——————————————————————————常量———————————————————————————#

cur_dir = os.path.dirname(os.path.realpath(__file__))
save_path = os.path.join(cur_dir, "pic")
Omega_m = 2 * pi
omega_c = 10 * Omega_m

#——————————————————————————函数———————————————————————————#

#—————————————————————————主程序——————————————————————————#

t = np.linspace(-3.2, 3.2, 10001)
y = (1 + 1.25 * cos(Omega_m * t))
mixed_y = y * cos(omega_c * t)
# iddim = np.where((mixed_y > 0) & (cos(omega_c * t) > 0.8))

# 检测极大值点
iddim = argrelextrema(mixed_y, np.greater)

plt.plot(t, y, label = "origin", linestyle = '--', color='orange')
plt.plot(t, -y, label = "-origin", linestyle = '--', color='orange')
plt.plot(t, mixed_y, label = "zaibo", color='blue')
plt.plot(t[iddim], mixed_y[iddim], label = 'detected', color='red')
plt.legend(loc="lower right")
plt.grid(True)
plt.xlabel("t")
plt.ylabel("yt")
plt.title("")
plt.show()