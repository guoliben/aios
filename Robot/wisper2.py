import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wavfile
import whisper

duration = 5  # 录音秒数
fs = 16000    # 采样率

print("开始录音...")
recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait()
print("录音结束")

wavfile.write("recorded.wav", fs, recording)

model = whisper.load_model("base")
result = model.transcribe("recorded.wav", language="zh")
print("识别结果:", result["text"])
