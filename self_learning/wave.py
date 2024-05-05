#——————————————————————————————生成波形信号并播放————————————————————————————————#


#——————————————————————————————————头文件——————————————————————————————————————#

import os
import numpy as np
from numpy import sin, cos, pi
from scipy.io import wavfile
from scipy.signal import spectrogram
import matplotlib.pyplot as plt
import sounddevice as sd
from time import sleep
import json

#———————————————————————————————————常量———————————————————————————————————————#

cur_dir = os.path.dirname(os.path.realpath(__file__))
const_filename = os.path.join(cur_dir, "yinfu.json")
const_file = open(const_filename, 'r')
yinfu_data = json.load(const_file)
music_filename = os.path.join(cur_dir, "玛丽有只小羊羔.txt")

#———————————————————————————————————函数———————————————————————————————————————#

def read_music_file() -> list:
    '''读取音乐文件'''
    music_file = open(music_filename, 'r')
    data_strings = music_file.readlines()
    freq_list, sec_list = [], []
    for s in data_strings:
        s = s.rstrip('\n')
        data = s.split(',')
        freq_list.append(data[0])
        sec_list.append(float(data[1]))
    return freq_list, sec_list

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

def generate_wave(sample_rate: int, sec: float, freq: float, func = sin, fudu = 1.):
    '''生成一个波形'''
    t = np.linspace(0, int(sample_rate * sec), num=int(sample_rate * sec)) / sample_rate
    return func(t * 2 * pi * freq) * fudu

def square(t):
    '''方波的运算,周期默认为2pi'''
    rt = np.zeros(np.shape(t))
    for i in range(1, 100):
        rt += 4 * sin(i * pi / 2) * cos(i * t) / (i * pi)
    return rt

def mixed_sin(t):
    '''调制后的波'''
    return sin(t) * square(t)


#——————————————————————————————————程序主体—————————————————————————————————————#


sample_rate = 44100
freq_list, sec_list = read_music_file()
std_sec = 0.7

# output_wave = np.zeros([0])

# for freq_key, sec in zip(freq_list, sec_list):
#     temp_wave = generate_wave(sample_rate, sec * std_sec, yinfu_data[freq_key], sin) * 3
#     output_wave = np.hstack([output_wave, temp_wave])

# 高中低音
high_wave = mid_wave = low_wave = np.zeros([0])
for freq_key, sec in zip(freq_list, sec_list):
    high_wave = np.hstack([high_wave, generate_wave(sample_rate, sec * std_sec, yinfu_data['h' + freq_key], sin) * 3])
    mid_wave = np.hstack([mid_wave, generate_wave(sample_rate, sec * std_sec, yinfu_data[freq_key], sin) * 3])
    low_wave = np.hstack([low_wave, generate_wave(sample_rate, sec * std_sec, yinfu_data['l' + freq_key], sin) * 3])

# output_wave = np.hstack([low_wave, mid_wave, high_wave])
output_wave = mid_wave * 0.33 + high_wave * 0.33 + low_wave * 0.33
# cnt_time(3, f"播放文件{music_filename}")
# play_audio(output_wave, sample_rate)


# 绘制播放音频的时频联合分布图
start_idx, end_idx = 0, 80
threshold = 20000
f, t, Sxx = spectrogram(output_wave, fs = sample_rate, nperseg=2048, nfft=2048)
# print(np.shape(f), np.shape(t), np.shape(Sxx))1

Sxx[Sxx > threshold] = threshold
plt.pcolormesh(t, f[start_idx: end_idx], Sxx[start_idx: end_idx,:])
plt.title(f"{music_filename}")
plt.xlabel("Time/s")
plt.ylabel("Frequence/Hz")
plt.show()