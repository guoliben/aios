# 1. 生成 TTS 音频并保存
from gtts import gTTS
import soundfile as sf
import sounddevice as sd

#tts = gTTS("你好，我是助手", lang='zh')
#tts.save("temp.wav")

## 2. 读取音频为 echo_buffer
#data, samplerate = sf.read("temp.wav", dtype='int16')
#echo_buffer = data[:, 0].tolist()  # 只取1通道
#sd.play(data, samplerate)
#print(data.ndim)




import numpy as np
import soundfile as sf



def get_data(waypath):
    # data 是你从 soundfile 读出来的数组
    data, samplerate = sf.read(waypath, dtype='int16')

    # 若为二维（立体声），取第一个通道；若为一维（单声道），直接使用
    if data.ndim == 2:
        echo_buffer = data[:, 0].tolist()
    else:
        echo_buffer = data.tolist()
    return data, samplerate, echo_buffer
    print(data)



def play_data(data, samplerate):
    # 3. 播放这段音频
    sd.play(data, samplerate)
    sd.wait()


from pyaec import Aec
frame_size = 256
filter_length = 2048
sample_rate = 16000

data1, samplerate1, buffer1 = (get_data("temp.wav"))
play_data(data1, samplerate1)

data2, samplerate2, buffer2 = (get_data("temp2.wav"))
play_data(data2, samplerate2)




assert samplerate1 == samplerate2 == sample_rate

aec = Aec(frame_size, filter_length, sample_rate)


min_len = min(len(buffer1), len(buffer2))
cleaned_output = []
for i in range(0, min_len - frame_size + 1, frame_size):
    frame_echo = buffer1[i:i + frame_size]
    frame_rec  = buffer2[i:i + frame_size]

    if len(frame_echo) != frame_size or len(frame_rec) != frame_size:
        continue  # 跳过长度不一致的残帧

    frame_clean = aec.cancel_echo(frame_rec, frame_echo)
    cleaned_output.extend(frame_clean)



# 播放处理后的结果
import numpy as np
cleaned_array = np.array(cleaned_output, dtype='int16')
sd.play(cleaned_array, sample_rate)
sd.wait()
sf.write("cleaned.wav", np.array(cleaned_output, dtype='int16'), 16000)



'''
from pyaec import Aec

# 假设每帧长度是 256，滤波器长度是 2048，采样率是 16000Hz
frame_size = 256
filter_length = 2048
sample_rate = 16000

aec = Aec(frame_size, filter_length, sample_rate)

# 模拟两个音频帧（整型 PCM 数据）
# rec_buffer 是带有回声的麦克风数据，echo_buffer 是参考信号（如扬声器输出）
rec_buffer = [1000] * frame_size  # 假数据
echo_buffer = [500] * frame_size  # 假数据

print(rec_buffer)
print(echo_buffer)

# 执行回声抵消
cleaned = aec.cancel_echo(rec_buffer, echo_buffer)

print("去回声后的数据:", cleaned)
'''
