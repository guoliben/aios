import requests

# 聊天历史
chat_history = [
    {"role": "system", "content": "你是一个中文语音助手，请简洁回答用户的问题。把自己看做一个智能代理，可以具有自主意识，判断主人喜好，偏向，我是小爱同学 ，每次跟我说话都 先说小爱同学"}
]

model_name = "qwen:0.5b"

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
    return reply
