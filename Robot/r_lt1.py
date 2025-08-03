import subprocess
import sounddevice as sd
import queue
import threading
import vosk
import json
from ctypes import *
from pyaec import Aec  # 你定义的AEC封装
import numpy as np
import os
import sys
import wave



q = queue.Queue()
lock = threading.Lock()
say_process = None

samplerate = 16000
frame_size = 1024

# 创建 AEC 实例
aec = Aec(frame_size=frame_size, filter_length=2048, sample_rate=samplerate)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "model-cn")
if not os.path.exists(model_path):
    print(f"❌ 模型路径不存在: {model_path}")
    sys.exit(1)

# VOSK识别器
model = vosk.Model(model_path)
rec = vosk.KaldiRecognizer(model, samplerate)

# 播放中的音频缓存
echo_buffer_queue = queue.Queue()

def callback(indata, frames, time, status):
    q.put(bytes(indata))

def play_audio_and_cache(text):
    """播放文本，同时缓存播放数据用于 AEC"""
    global say_process

    # 使用 say 命令将 text 合成为 wav
    subprocess.run(['say', '-o', 'out.aiff', text])
    subprocess.run(['ffmpeg', '-y', '-i', 'out.aiff', '-ar', '16000', '-ac', '1', '-f', 's16le', 'out.raw'])

    with open('out.raw', 'rb') as f:
        while True:
            data = f.read(frame_size * 2)  # 2字节 per sample
            if not data:
                break
            echo_buffer_queue.put(data)
            sd.play(np.frombuffer(data, dtype=np.int16), samplerate=samplerate, blocking=True)

def Talk(text):
    if not text.strip():
        return
    print(f"🤖 回答：{text}")
    # t = threading.Thread(target=play_audio_and_cache, args=(text,))
    # t.start()
    play_audio_and_cache(text)

def Listen_to_me():
    with sd.RawInputStream(samplerate=samplerate, blocksize=frame_size * 2, dtype='int16',
                           channels=1, callback=callback):
        print("🎤 正在聆听（说话后暂停自动识别）...")
        while True:
            rec_data = q.get()

            # text = is_speech(rec_data)
            # if len(text) <= 0:
                # print("未检测到人声")
                # continue

            echo_data = echo_buffer_queue.get() if not echo_buffer_queue.empty() else b'\x00' * len(rec_data)

            # 转为 short list
            rec_frame = list(np.frombuffer(rec_data, dtype=np.int16))
            echo_frame = list(np.frombuffer(echo_data, dtype=np.int16))


            # print(f"rec_frame length: {len(rec_frame)}")
            # print(f"echo_frame length: {len(echo_frame)}")
            # print(f"frame_size length: {frame_size * 2}")
            #
            # if len(echo_frame) < len(rec_frame):
            #     # 用静音补齐
            #     pad_len = len(rec_frame) - len(echo_frame)
            #     echo_frame += [0] * pad_len
            # elif len(echo_frame) > len(rec_frame):
            #     echo_frame = echo_frame[:len(rec_frame)]
            #

            if len(rec_frame) != (frame_size * 2) or len(echo_frame) != (frame_size * 2):
                print("帧长不一致，跳过")
                continue

            # AEC
            try:
                # print("回声降噪中...")
                # cleaned = aec.cancel_echo(rec_frame, echo_frame)
                cleaned = rec_frame
            except Exception as e:
                print("AEC失败:", e)
                continue

            cleaned_bytes = np.array(cleaned, dtype=np.int16).tobytes()
            append_to_wav("s2.wav", cleaned_bytes)
            if rec.AcceptWaveform(cleaned_bytes):
                result = json.loads(rec.Result())
                text = result.get("text", "")
                if text:
                    print(f"🗣️  你说：{text}")
                else:
                    print("❌ 无法识别语音。")
                return text


# def write_frame(filepath, new_data):
#     with wave.open(filepath, 'ab') as wf:  # 二进制追加
#         wf.writeframes(new_data.tobytes())  # 直接追加PCM数据

def append_to_wav(filepath: str, new_frames: bytes):
    """
    把原有 WAV 文件的 PCM 数据和 new_frames 拼接，
    然后以 wb 模式重写整个文件（更新 header）。
    """
    if os.path.exists(filepath):
        # 1. 读出原有数据
        with wave.open(filepath, 'rb') as rf:
            params = rf.getparams()       # 保存原来的声道、采样率、样本宽度等
            old_frames = rf.readframes(rf.getnframes())
    else:
        # 如果文件不存在，直接写新的
        old_frames = b''
        # 这里设定你的默认参数（双声道/单声道、采样宽度、采样率）
        params = wave._wave_params(nchannels=1, sampwidth=2, framerate=16000,
                                   nframes=0, comptype='NONE', compname='not compressed')

    # 2. 拼接 PCM 数据
    combined = old_frames + new_frames

    # 3. 以 wb 模式写回（header 会自动根据 combined 长度更新 nframes）
    with wave.open(filepath, 'wb') as wf:
        wf.setnchannels(params.nchannels)
        wf.setsampwidth(params.sampwidth)
        wf.setframerate(params.framerate)
        wf.writeframes(combined)



def is_speech(audio_bytes: bytes) -> str:
    if rec.AcceptWaveform(audio_bytes):
        result = json.loads(rec.Result())
        text = result.get("text", "").strip()
        return text
    else:
        # 可选：partial 也可以识别
        partial_result = json.loads(rec.PartialResult())
        partial = partial_result.get("partial", "").strip()
        return partial

while True:
    command = Listen_to_me()
    Talk(command)

# 示例使用
# while True:
#     with sd.RawInputStream(samplerate=samplerate, blocksize=frame_size * 2, dtype='int16',
#                            channels=1, callback=callback):
#         print("🎤 正在聆听（说话后暂停自动识别）...")
#         while True:
#             rec_data = q.get()  # 从录音队列中取出原始 PCM 数据
#             text = is_speech(rec_data)
#             if len(text) > 0:
#                 print("✅ 检测到人声", text)
#             # else:
#                 # print("❌ 没有人声")