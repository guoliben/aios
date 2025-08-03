import pyaec
# 初始化 echo canceller
aec = pyaec.EchoCanceller(frame_size=256, filter_length=2048, sample_rate=16000)
clean_frame = aec.process(near_buffer, far_buffer)  # float32 numpy arrays
