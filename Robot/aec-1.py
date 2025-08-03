import sounddevice as sd
import queue
import json
import threading
import os
from TTS.api import TTS
from vosk import Model, KaldiRecognizer

# 初始化队列与模型
q = queue.Queue()
vosk_model = Model("tts_models")  # 替换成你的路径
recognizer = KaldiRecognizer(vosk_model, 16000)
# tts_models/zh-CN/baker/tacotron2-DDC-GST   pip install tts &   tts --list_models
tts = TTS(model_name="tts_models/zh-CN/baker/tacotron2-DDC-GST", progress_bar=False)

# 音频设备名（用 `sd.query_devices()` 查看）
AEC_INPUT = "Echo-Cancel Source"
AEC_OUTPUT = "Echo-Cancel Sink"

# 回调函数处理音频流
def audio_callback(indata, frames, time, status):
    if status:
        print(f"⚠️ 错误：{status}")
    q.put(bytes(indata))

# TTS 播放线程
def play_tts(text):
    if not text.strip():
        return
    print(f"🤖 回复：{text}")
    tts.tts_to_file(text=text, file_path="output.wav")
    os.system(f"paplay --device='{AEC_OUTPUT}' output.wav")

# 语音识别线程
def recognize_loop():
    print("🎤 开始识别，按 Ctrl+C 停止")
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=audio_callback, device=AEC_INPUT):
        while True:
            data = q.get()
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                text = result.get("text", "")
                if text:
                    print(f"🗣️ 你说：{text}")
                    # 触发 TTS 响应
                    threading.Thread(target=play_tts, args=(f"你说的是：{text}",)).start()

# 启动识别
recognize_loop()
