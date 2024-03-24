#——————————对图像进行去除模糊的操作————————————#

# 先导入图像并对其进行操作
from scipy.io import loadmat

data = loadmat('/home/tianxj/myCode/homework/xinhaoyuxitong/4/imagedata.mat')

# print(data.keys())

for k, v in data.items():
    print(f"{k}: {v}")

import cv2

def show_img(window_name: str, img):
    cv2.imshow(window_name, img)
    cv2.waitKey()
    cv2.destroyAllWindows()
    print(img)
    cv2.imwrite(f'/home/tianxj/myCode/homework/xinhaoyuxitong/4/exp1/{window_name}.jpg', img.copy() * 255)

show_img('source img', data['I'])
# 乘以255可以将数值的差异变得明显
show_img('PSf', data['PSf'].copy() * 255)
show_img('blurred', data['blurred'])

# 模拟卷积操作，验证图像准确性
operated_img = cv2.filter2D(data['I'], -1, data['PSf'])
show_img('operated_img', operated_img)

# 下面进行去除模糊的操作

# 这里的deconvwnr函数由ChatGPT生成。因为python中没有和matlab中这个函数完全一样的函数
import numpy as np
from scipy.signal import convolve2d
from numpy.fft import fft2, ifft2, fftshift

def deconvwnr(blurred_img, psf, snr):
    """
    使用Wiener滤波进行解卷积，类似于MATLAB的deconvwnr函数。
    
    参数：
    - blurred_img: 模糊的图像
    - psf: 点扩散函数
    - snr: 信噪比
    
    返回：
    - deconvolved_img: 解卷积后的图像
    """
    # 对图像和PSF进行傅里叶变换
    blurred_img_fft = fft2(blurred_img)
    psf_fft = fft2(psf, s=blurred_img.shape)
    
    # 计算Wiener滤波
    H_conj = np.conj(psf_fft)
    # 注意：这里假设snr是信号与噪声的功率比
    wiener_filter = H_conj / (np.abs(psf_fft)**2 + 1/snr)
    
    # 应用Wiener滤波
    deconv_fft = wiener_filter * blurred_img_fft
    
    # 逆傅里叶变换回到空间域
    deconvolved_img = np.real(ifft2(deconv_fft))
    
    return deconvolved_img


snr = 10000000000
cleared_photo = deconvwnr(data['blurred'], data['PSf'], snr)
show_img('cleared_photo', cleared_photo.copy())