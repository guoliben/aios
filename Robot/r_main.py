# from r_listen import Listen_to_me
# from r_listen import listen_speech_vosk
from r_lt1 import  Listen_to_me, Talk
from r_qwen import Chat_with_ollama
from r_talk import Talk
# 主程序
def main():
    print("🚀 启动语音助手：Vosk + Ollama + TTS（全本地）")
    echos = ""
    while True:
        try:
            user_input = Listen_to_me()
            if not user_input:
                continue
            print("---->")
            print(user_input.replace(" ", "").replace(echos, ""))
            print("<----")
            ai_reply = Chat_with_ollama(user_input.replace(" ", "").replace(echos, ""))
            Talk(ai_reply)
            echos = ai_reply.replace(" ", "").replace(echos, "").replace("，", "").replace("。", "")
        except KeyboardInterrupt:
            print("\n👋 程序退出。")
            break


if __name__ == "__main__":
    main()