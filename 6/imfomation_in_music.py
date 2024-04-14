#————————音频中的幅频和相位特性——————————#

#——————————————头文件—————————————————#

import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import sounddevice as sd
from time import sleep

#—————————————全局变量————————————————#

# 图片路径
program_root = os.path.dirname(os.path.realpath(__file__))
music_root = os.path.join(program_root, 'XIHaiLoveSong.wav')
img_save_root = os.path.join(program_root, 'graph')
music__save_root = os.path.join(program_root, 'music')

# 声音极限
sound_threshold = 30000

#———————————————函数—————————————————#

def play_audio(rll: list, fs: int):
    '''播放音乐'''
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


#——————————————程序主体——————————————#

sample_rate, sig = wavfile.read(music_root)
# print(sample_rate, np.shape(sig))
# 获取幅度谱和相位谱
sigfft = np.fft.fft(sig)
sig_A = np.fft.ifft(abs(sigfft))
sig_A[abs(sig_A) > sound_threshold] = sound_threshold
sig_theta = np.fft.ifft(sigfft / abs(sigfft) * 1e7)
sig_theta[abs(sig_theta) > sound_threshold] = sound_threshold

plt.subplot(2, 2, 1)
plt.title("origin")
plt.plot(sig)
# plt.show()
plt.subplot(2, 2, 2)
plt.title("fudu")
plt.plot(sig_A)
# plt.show()
plt.subplot(2, 2, 3)
plt.title("xiangwei")
plt.plot(sig_theta.real)
plt.show()

# plt.title("origin signal and its fudu and xiangwei pu")
# plt.xlabel('sample')
# plt.ylabel('Wave')
# plt.grid(True)
# plt.show()
# plt.savefig(os.path.join(img_save_root, 'wav_info.jpg'))

# cnt_time(5, '播放原音乐')
# play_audio(sig[0: 5 * sample_rate], sample_rate)
# wavfile.write(os.path.join(music__save_root, 'origin.wav'), sample_rate, sig)

# cnt_time(5, '播放幅度谱恢复音乐')
# play_audio(sig_A[0: 5 * sample_rate].real, sample_rate)
# wavfile.write(os.path.join(music__save_root, 'fudu.wav'), sample_rate, sig_A.real)

# cnt_time(5, '播放相位谱恢复音乐')
# play_audio(sig_theta[0: 5 * sample_rate].real, sample_rate)
# wavfile.write(os.path.join(music__save_root, 'xiangwei.wav'), sample_rate, sig_theta.real)