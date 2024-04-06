#————————照片中的幅频和相位特性——————————#

#——————————————头文件—————————————————#

import os
import cv2
import numpy as np
from cv2.typing import *
import matplotlib.pyplot as plt

#—————————————全局变量————————————————#

# 图片路径
program_root = os.path.dirname(os.path.realpath(__file__))
img_root = os.path.join(program_root, 'origin.jpg')
save_root = os.path.join(program_root, 'graph')

#———————————————函数—————————————————#

def show_image(img: MatLike, windows_name: str):
    '''展示图片'''
    cv2.imshow(windows_name, img)
    cv2.waitKey()
    cv2.destroyAllWindows()

def save_image(img: MatLike, filename: str, photo_type = 'jpg'):
    '''存储图片'''
    root = os.path.join(save_root, f'{filename}.{photo_type}')
    cv2.imwrite(root, img)

#——————————————程序主体——————————————#

img = cv2.imread(img_root)
# show_image(img, 'origin')

# 灰度处理
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
save_image(gray, 'gray')
# show_image(gray, 'gray')

# 做傅里叶变换，得到幅度谱和相位谱
imgfft = np.fft.fft2(gray)
# print(np.shape(imgfft), type(imgfft))

imgabs = abs(imgfft)
# 防止溢出
imgabs[imgabs > 20000] = 20000
imgangle = np.angle(imgfft)

# 展示幅度和相位图片
plt.subplot(1, 2, 1)
plt.title('fudu')
plt.imshow(imgabs)
plt.subplot(1, 2, 2)
plt.title('xiangwei')
plt.imshow(imgangle)
plt.show()


# 用幅度恢复图像
img0 = np.fft.ifft2(imgfft)
img1 = np.fft.ifft2(imgabs)
img1[img1 > 255] = 255

plt.subplot(1, 2, 1)
plt.title('origin')
plt.imshow(abs(img0))
plt.subplot(1, 2, 2)
plt.title('fudu')
plt.imshow(abs(img1))
plt.savefig(os.path.join(save_root, 'fudu.jpg'))
plt.show()

# 用相位恢复图像
img2 = np.fft.ifft2(imgfft / imgabs)
plt.subplot(1, 2, 1)
plt.title('origin')
plt.imshow(abs(img0))
plt.subplot(1, 2, 2)
plt.title('xiangwei')
plt.imshow(abs(img2))
plt.savefig(os.path.join(save_root, 'xiangwei.jpg'))
plt.show()