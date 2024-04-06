#——————————测试高低频的音乐————————————#

#——————————————头文件—————————————————#

import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import sounddevice as sd
from time import sleep
import random

#—————————————全局变量————————————————#

# 图片路径
program_root = os.path.dirname(os.path.realpath(__file__))
music_root = os.path.join(program_root, 'XIHaiLoveSong.wav')
img_save_root = os.path.join(program_root, 'graph')
music__save_root = os.path.join(program_root, 'music')

# 声音极限
sound_threshold = 300

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

sample_rate = 44100
sig = []
for n in range(0, 5):
    for i in range(0, sample_rate):
        sig.append(float(random.randrange(0, 30000)))

# print(sig)
play_audio(sig, sample_rate)