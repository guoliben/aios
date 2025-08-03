
import pyttsx3

engine = pyttsx3.init()

# 列出所有语音
voices = engine.getProperty('voices')
for idx, voice in enumerate(voices):
    print(f"{idx}: {voice.name} ({voice.languages}) - {voice.id}")

# 选择语音（比如中文女声、男声等）
engine.setProperty('voice', voices[151].id)  # 替换成合适的 index

# 朗读文本
engine.say("你好，这是一个中文朗读测试")
engine.runAndWait()




import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)  # 语速
engine.setProperty('volume', 1.0)  # 音量（0~1）

text = "你好，欢迎使用 Python 文本朗读功能！"
engine.say(text)
engine.runAndWait()

