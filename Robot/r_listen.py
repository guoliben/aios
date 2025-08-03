import sounddevice as sd
import vosk
import queue
import json
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "model-cn")
# model_path = "model-cn"  # 确保此路径下有模型文件夹
if not os.path.exists(model_path):
    print(f"❌ 模型路径不存在: {model_path}")
    sys.exit(1)

model = vosk.Model(model_path)

q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(f"⚠️ 状态警告: {status}")
    q.put(bytes(indata))

def listen_speech_vosk():
    samplerate = 16000
    blocksize = 8000
    rec = vosk.KaldiRecognizer(model, samplerate)

    with sd.RawInputStream(samplerate=samplerate, blocksize=blocksize, dtype='int16',
                           channels=1, callback=callback):
        print("🎤 正在聆听（说话后暂停自动识别）...")
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "")
                if text:
                    print(f"🗣️ 你说：{text}")
                else:
                    print("❌ 无法识别语音。")
                return text

def Listen_to_me():
    samplerate = 16000
    blocksize = 8000
    rec = vosk.KaldiRecognizer(model, samplerate)

    with sd.RawInputStream(samplerate=samplerate, blocksize=blocksize, dtype='int16',
                           channels=1, callback=callback):
        print("🎤 正在聆听（说话后暂停自动识别）...")
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "")
                if text:
                    print(f"🗣️ 你说：{text}")
                else:
                    print("❌ 无法识别语音。")
                return text


def listen_with_echoless():
	print("=============echo less ")




listen_with_echoless()


