import os

def speak_text(text):
    print(f"🤖 回答：{text}")
    os.system(f'say "{text}"')  # macOS 原生命令
