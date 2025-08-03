import sounddevice as sd

print(sd.query_devices())  # 查看设备列表
sd.default.device = 1  # 选对麦克风编号
duration = 3  # 秒
fs = 16000  # 采样率
audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
sd.wait()
print("录音完成")
