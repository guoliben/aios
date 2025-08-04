import subprocess, threading
import time
# say_process = None
# lock = threading.Lock()
#
# def Talk_1(text):
#     if not text.strip():
#         return
#     print(f"🤖 回答?：{text}")
#     global say_process
#     with lock:
#         # 如果有旧的语音进程，在开始新朗读前终止
#         if say_process and say_process.poll() is None:
#             say_process.terminate()
#             say_process = None
#
#         print(f"🤖 回答：{text}")
#         say_process = subprocess.Popen(['say', text])
#

def Talk(text, chosen_voice):
    # if not text.strip():
    #     return
    # print(f"🤖 回答?：{text}")
    # subprocess.Popen(['say', text])
    #
    if not text.strip():
        return
    print(f"🤖 回答：{text}")
    subprocess.run(['say', text])  # ✅ 等待播报结束再继续
    # subprocess.run(['say', '-v', chosen_voice, text])


# from TTS.api import TTS
# import sounddevice as sd
#
# tts = TTS(model_name="tts_models/zh-CN/baker/tacotron2-DDC-GST", progress_bar=False, gpu=False)
#
# def speak(text):
#     wav = tts.tts(text)
#     sd.play(wav, samplerate=22050)
#     sd.wait()  # 等待播放完毕
# speak("1121321")