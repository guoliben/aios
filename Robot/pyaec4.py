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
