import numpy as np
import pyaec


print(pyaec)
# 创建 Echo Canceller：frame_size=256, filter_length=2048, sample_rate=16000
#ec = pyaec.EchoCanceller(256, 2048, 16000)

# 假设 near_buf 和 far_buf 是长度256的 numpy float32 音频帧
#clean = ec.process(near_buf, far_buf)
