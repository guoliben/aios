import soundfile as sf
import matplotlib.pyplot as plt
import numpy as np



#
# # 读取三段音频
# rec_data, sr1 = sf.read("temp2.wav", dtype='int16')      # 含回声
# echo_data, sr2 = sf.read("temp.wav", dtype='int16')      # 外放声
# cleaned_data, sr3 = sf.read("cleaned.wav", dtype='int16')# 去回声结果
#
# # 确保全为单通道
# if rec_data.ndim == 2:
#     rec_data = rec_data[:, 0]
# if echo_data.ndim == 2:
#     echo_data = echo_data[:, 0]
# if cleaned_data.ndim == 2:
#     cleaned_data = cleaned_data[:, 0]

# # 生成时间轴（秒）
# time_rec = np.linspace(0, len(rec_data) / sr1, num=len(rec_data))
# time_echo = np.linspace(0, len(echo_data) / sr2, num=len(echo_data))
# time_cleaned = np.linspace(0, len(cleaned_data) / sr3, num=len(cleaned_data))


def read_wave(file_name):
    read_data, sr = sf.read(file_name, dtype='int16')
    if read_data.ndim == 2:
        read_data = read_data[:, 0]

    time_data = np.linspace(0, len(read_data) / sr, num=len(read_data))
    return read_data, time_data


# 画图
plt.figure(figsize=(14, 10))
d, t = read_wave("temp.wav")
plt.subplot(4, 1, 1)
plt.plot(t, d, color='orange')
plt.title("含回声录音（temp2.wav）")
plt.ylabel("Amplitude")
plt.xlabel("Time (s)")

d, t = read_wave("temp2.wav")
plt.subplot(4, 1, 2)
plt.plot(t, d, color='blue')
plt.title("外放源音频（temp.wav）")
plt.ylabel("Amplitude")
plt.xlabel("Time (s)")

#
# d, t = read_wave("cleaned.wav")
# plt.subplot(4, 1, 3)
# plt.plot(t, d, color='green')
# plt.title("去回声结果（cleaned.wav）")
# plt.ylabel("Amplitude")
# plt.xlabel("Time (s)")


d, t = read_wave("s1.wav")
plt.subplot(4, 1, 3)
plt.plot(t, d, color='red')
plt.title("去回声结果（s1.wav）")
plt.ylabel("Amplitude")
plt.xlabel("Time (s)")


d, t = read_wave("s2.wav")
plt.subplot(4, 1, 4)
plt.plot(t, d, color='red')
plt.title("去回声结果（s2.wav）")
plt.ylabel("Amplitude")
plt.xlabel("Time (s)")


plt.tight_layout()
plt.show()





#say "hello hello" -o temp.aiff
#ffmpeg -i temp.aiff -ar 16000 -ac 1 -f wav -acodec pcm_s16le temp.wav
