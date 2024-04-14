#——————————将音乐截取前六秒——————————#

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

#——————————————————————————————————函数——————————————————————————————————————#

#—————————————————————————————————程序主体————————————————————————————————————#

for wav_file in wav_files:
    print(f"现在截取音乐文件{wav_file}")
    sample_rate, sig = wavfile.read(os.path.join(src_dir, wav_file))
    wavfile.write(os.path.join(src_dir, wav_file), sample_rate, sig[0: sample_rate * 6,:])