import aec

# 初始化
frame_size = 256
filter_length = 2048
sample_rate = 16000

echo_canceller = aec.EchoCanceller(frame_size, filter_length, sample_rate)

# 输入近端（麦克风捕获）和远端（播放音频）帧
# 这里的 data_near 和 data_far 都是 numpy 数组，类型 float32，长度 frame_size
output = echo_canceller.process(data_near, data_far)
