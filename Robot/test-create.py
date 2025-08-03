import requests


model_name = "qwen:0.5b"

# 聊天历史记录
chat_history = [
    {"role": "system", "content": "你是一个语音助手，简洁、用中文回答问题。"}
]

def chat_with_ollama(prompt):
    chat_history.append({"role": "user", "content": prompt})
    payload = {
        "model": model_name,
        "messages": chat_history,
        "stream": False
    }

    response = requests.post("http://127.0.0.1:11434/api/chat", json=payload)
    print(f"status: {response.status_code}, text: {response.text}")
    #
    # response = requests.post("http://127.0.0.1:11434/api/chat", json=payload)
    # print(response)
    if response.status_code != 200:
        raise RuntimeError(f"Ollama 请求失败: {response.status_code}, {response.text}")

    reply = response.json()["message"]["content"]
    chat_history.append({"role": "assistant", "content": reply})
    return reply


ai_reply = chat_with_ollama("你是谁")
print(ai_reply)
