import requests

# 聊天历史
chat_history = [
    {"role": "system", "content": "你是AI语音助手 每次回答问题简短，不要超过30个字 回答问题 不要用表情符号"}
]

model_name = "qwen:1.8b"
model_name = "gemma3:1b"

def Chat_with_ollama(prompt):
    chat_history.append({"role": "user", "content": prompt})
    payload = {
        "model": model_name,
        "messages": chat_history,
        "stream": False
    }

    response = requests.post("http://127.0.0.1:11434/api/chat", json=payload)
    # print(f"status: {response.status_code}, text: {response.text}")
    if response.status_code != 200:
        raise RuntimeError(f"Ollama 请求失败: {response.status_code}, {response.text}")

    reply = response.json()["message"]["content"]
    chat_history.append({"role": "assistant", "content": reply})
    return "小爱同学 ， " + reply


# (p r_main.py &) && (p r_main.py &)