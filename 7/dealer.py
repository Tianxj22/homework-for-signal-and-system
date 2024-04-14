#————————————————————————生成相关信号的时频联合分布图————————————————————————————#

#————————————————————————————————头文件——————————————————————————————————————#

import os
import numpy as np
from scipy.io import wavfile
from scipy.signal import spectrogram
import matplotlib.pyplot as plt
import sounddevice as sd
from time import sleep

#——————————————————————————————————全局变量——————————————————————————————————#

cur_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(cur_dir, 'HW6DATA')

music_files = os.listdir(src_dir)
music_files.sort()
wav_files = []
for file in music_files:
    if file.split('.')[-1] == 'wav':
        wav_files.append(file)

start_idx, end_idx = 20, 120
threshold = 20000

#——————————————————————————————————函数——————————————————————————————————————#

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

def deal_single_file(file: str):
    '''将单个音频文件的时频图绘制'''
    sample_rate, sig = wavfile.read(os.path.join(src_dir, file))
    sig = sig[0: sample_rate * 5, 0]
    f, t, Sxx = spectrogram(sig, fs = sample_rate, nperseg=2048, nfft=2048)
    
    Sxx[Sxx > threshold] = threshold
    plt.pcolormesh(t, f[start_idx: end_idx], Sxx[start_idx:end_idx,:])
    plt.title(f"{file}")
    plt.xlabel("Time/s")
    plt.ylabel("Frequence/Hz")

#—————————————————————————————————程序主体————————————————————————————————————#


col = 3
row = int(len(wav_files) / 3)
if len(wav_files) % 3:
    row += 1
for i in range(len(wav_files)):
    plt.subplot(row, col, i + 1)
    print(f"处理文件{wav_files[i]}")
    deal_single_file(wav_files[i])
plt.show()