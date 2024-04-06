import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# 读取音频文件
# 替换 'your_audio_file.wav' 为你的音频文件路径
filename = '/home/tianxj/myCode/homework/xinhaoyuxitong/1/homework1.mp3'
sounddata, fs = librosa.load(filename, sr=None) # sr=None 确保以原始采样率加载

# 计算短时傅里叶变换 (STFT)
n_fft = 4096
hop_length = 2048 # 窗口重叠
D = librosa.stft(sounddata, n_fft=n_fft, hop_length=hop_length)

# 将STFT的幅度转换为分贝 (dB)
D_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)

# 绘制频谱图
plt.figure(figsize=(19, 6))
librosa.display.specshow(D_db, sr=fs, hop_length=hop_length, x_axis='time', y_axis='log', fmin=500, fmax=2000)
plt.ylim(bottom=400, top=3000)
plt.colorbar(format='%+2.0f dB')
plt.title('Spectrogram')
plt.savefig("/home/tianxj/myCode/homework/xinhaoyuxitong/1/graph/16.png")
plt.show()