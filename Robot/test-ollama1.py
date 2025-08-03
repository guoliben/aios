import openai
import speech_recognition as sr
import pyttsx3

# 🧠 使用 Ollama 的 deepseek-coder:1.5b 模型
openai.api_base = "http://localhost:11434/v1"
openai.api_key = "ollama"  # 任意字符串即可
model_name = "deepseek-coder:1.5b"

# 初始化语音合成引擎
tts = pyttsx3.init()
tts.setProperty('rate', 170)  # 语速

# 初始化语音识别器
recognizer = sr.Recognizer()

# 聊天历史记录
chat_history = [
    {"role": "system", "content": "你是一个语音助手，简洁、用中文回答问题。"}
]

def listen_speech():
    with sr.Microphone() as source:
        print("🎤 等待语音输入...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language="zh-CN")
        print(f"🗣️ 你说：{text}")
        return text
    except sr.UnknownValueError:
        print("❌ 无法识别语音。")
        return ""
    except Exception as e:
        print(f"❌ 语音识别错误: {e}")
        return ""

def speak_text(text):
    print(f"🤖 AI 回应：{text}")
    tts.say(text)
    tts.runAndWait()

def chat_with_ollama(prompt):
    chat_history.append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(
        model=model_name,
        messages=chat_history
    )
    reply = response['choices'][0]['message']['content']
    chat_history.append({"role": "assistant", "content": reply})
    return reply

# 主循环
while True:
    try:
        user_input = listen_speech()
        if not user_input:
            continue
        ai_reply = chat_with_ollama(user_input)
        speak_text(ai_reply)
    except KeyboardInterrupt:
        print("\n👋 程序退出。")
        break