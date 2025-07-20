# import speech_recognition as sr
#
# # brew install portaudio && pip install pyaudio
#
# # 初始化识别器
# r = sr.Recognizer()
#
# # 使用默认麦克风作为音源
# with sr.Microphone() as source:
#     print("请开始讲话...")
#     r.adjust_for_ambient_noise(source)  # 降噪
#     audio = r.listen(source)
#     print("识别中...")
#
# try:
#     # 使用 Google Web 语音识别服务
#     text = r.recognize_google(audio, language='zh-CN')  # 中文识别
#     print("识别结果：", text)
# except sr.UnknownValueError:
#     print("无法识别音频")
# except sr.RequestError as e:
#     print("无法请求服务；{0}".format(e))


import speech_recognition as sr

# 初始化识别器
r = sr.Recognizer()

# 使用默认麦克风作为音源
with sr.Microphone() as source:
    print("开始语音识别（按 Ctrl+C 停止）...")
    r.adjust_for_ambient_noise(source)  # 自动降噪

    while True:
        print("\n请开始讲话...")
        try:
            audio = r.listen(source, timeout=5)  # 最多等待5秒开始讲话
            print("识别中...")

            text = r.recognize_google(audio, language='zh-CN')
            print("识别结果：", text)

        except sr.WaitTimeoutError:
            print("等待超时，没有检测到语音输入。")
        except sr.UnknownValueError:
            print("无法识别音频")
        except sr.RequestError as e:
            print("无法请求服务；{0}".format(e))