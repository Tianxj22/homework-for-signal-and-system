#————————音乐处理——————————#

from scipy.io import loadmat

file_path = '/home/tianxj/myCode/homework/xinhaoyuxitong/4/echodata.mat'
data = loadmat(file_path)

for k, v in data.items():
    print(f"{k}: {v}")

# 尝试播放音乐
import numpy as np
import sounddevice as sd
from time import sleep

def play_audio(rll: list, fs: int):
    sound_data = np.array(rll)

    # 播放音频文件
    sd.play(sound_data, fs)
    sd.wait()

def cnt_time(time_limit: int, event: str):
    '''时间倒计时'''
    print(f"{time_limit}秒后将{event}")
    cnt = time_limit
    while cnt > 0:
        print(cnt)
        cnt -= 1
        sleep(1)

rll = data['rll'].flatten()
fs = data['fs']
psf = data['psf'].flatten()

cnt_time(5, "播放原声")
play_audio(rll, fs)
cnt_time(5, "播放回声系统单位冲激响应信号")
play_audio(psf, fs)

backsound = np.convolve(rll.copy(), psf.copy())
cnt_time(5, "播放合成音乐")
play_audio(backsound, fs)

import numpy as np
from scipy.signal import convolve2d
from numpy.fft import fft, ifft, fft2

def deconvwnr(blurred, psf, snr):
    """
    使用Wiener滤波进行解卷积，类似于MATLAB的deconvwnr函数。
    
    参数：
    - blurred: 模糊的音频
    - psf: 点扩散函数
    - snr: 信噪比
    
    返回：
    - deconvolved: 解卷积后的音频
    """
    # 对音频和PSF进行傅里叶变换
    blurred_fft = fft(blurred)
    psf_fft = fft(psf)

    # 计算Wiener滤波
    H_conj = np.conj(psf_fft)
    # 注意：这里假设snr是信号与噪声的功率比
    wiener_filter = H_conj / (np.abs(psf_fft)**2 + 1/snr)
    
    # 应用Wiener滤波
    deconv_fft = wiener_filter * blurred_fft
    
    # 逆傅里叶变换回到空间域
    deconvolved = np.real(ifft(deconv_fft))
    
    return deconvolved

snr = 10000
print(len(backsound), len(psf))
psf = np.insert(psf, len(psf), np.zeros(len(backsound) - len(psf)))
recover = deconvwnr(backsound, psf, snr)
cnt_time(5, "播放恢复后的音乐")
play_audio(recover, fs)