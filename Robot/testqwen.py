import time
import threading
import subprocess

from openai import OpenAI
import speech_recognition as sr
import pyttsx3
import requests


# 初始化 openai 客户端
client = OpenAI(
    base_url="http://127.0.0.1:11434/api/chat",
    api_key="ollama"  # 任意非空字符串即可
)

model_name = "qwen:0.5b"

# 初始化语音合成
# tts = pyttsx3.init()

tts = pyttsx3.init(driverName='nsss')  # Windows
tts.setProperty('rate', 170)


import os


# 初始化语音识别
recognizer = sr.Recognizer()

# 聊天历史
chat_history = [
    {"role": "system", "content": "你是一个中文语音助手，请简洁回答用户的问题。把自己看做一个智能代理，可以具有自主意识，判断主人喜好，偏向"}
]


say_process = None
lock = threading.Lock()

def speak_text(text):
    if not text.strip():
        return
    print(f"🤖 回答?：{text}")
    global say_process
    with lock:
        # 如果有旧的语音进程，在开始新朗读前终止
        if say_process and say_process.poll() is None:
            say_process.terminate()
            say_process = None

        print(f"🤖 回答：{text}")
        say_process = subprocess.Popen(['say', text])

#
# def speak_text(text):
#     print(f"🤖 回答：{text}")
#     os.system(f'say "{text}"')  # macOS 原生命令

#
# def speak_text(text):
#     print(f"🤖 回答：{text}")
#     tts.say(text)
#     tts.runAndWait()


def listen_speech():
    try:
        text = input("⌨️ 请输入你要说的话：")
        print(f"🗣️ 你输入：{text}")
        return text.strip()
    except Exception as e:
        print(f"❌ 错误: {e}")
        return ""

def listen_speech_lis():
    with sr.Microphone() as source:
        print("🎤 正在聆听...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language="zh-CN")
        print(f"🗣️ 你说：{text}")
        return text
    except sr.UnknownValueError:
        print("❌ 无法识别语音。")
        return ""
    except Exception as e:
        print(f"❌ 错误: {e}")
        return ""


def chat_with_ollama(prompt):
    chat_history.append({"role": "user", "content": prompt})
    payload = {
        "model": model_name,
        "messages": chat_history,
        "stream": False
    }

    response = requests.post("http://127.0.0.1:11434/api/chat", json=payload)
    print(f"status: {response.status_code}, text: {response.text}")
    if response.status_code != 200:
        raise RuntimeError(f"Ollama 请求失败: {response.status_code}, {response.text}")

    reply = response.json()["message"]["content"]
    chat_history.append({"role": "assistant", "content": reply})
    return reply

# 主循环
while True:
    try:
        user_input = listen_speech_lis()
        if not user_input:
            continue
        ai_reply = chat_with_ollama(user_input)
        speak_text(ai_reply)
    except KeyboardInterrupt:
        print("\n👋 程序退出。")
        break



