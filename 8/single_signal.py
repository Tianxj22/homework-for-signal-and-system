#——————————————————————————————单边带信号模拟——————————————————————————————#


#—————————————————————————————————头文件——————————————————————————————————#

import matplotlib.pyplot as plt
from random import *
import numpy as np

#——————————————————————————————————常量——————————————————————————————————#

# 码流的大小
bite_num = 50
# 1bite数据传输的时间
during_sec = 5

#——————————————————————————————————函数——————————————————————————————————#


#——————————————————————————————————主体——————————————————————————————————#

# 生成码流
bite_string = [randint(0, 1) for _ in range(bite_num)]
print(bite_string)

# 绘制码流图
t = np.linspace(0, during_sec * bite_num, bite_num * 100)
y = [bite_string[int(ti / during_sec) - 1] for ti in t]
plt.plot(t, y)
plt.grid(True)
plt.show()