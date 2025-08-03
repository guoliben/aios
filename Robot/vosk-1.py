from vosk import Model, KaldiRecognizer
import pyaudio
import json

def listen_speech_lis():
    model_path = "model-cn"  # 中文模型目录
    model = Model(model_path)
    rec = KaldiRecognizer(model, 16000)

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1, rate=16000, input=True,
                    frames_per_buffer=8000)
    stream.start_stream()

    print("🎤 正在聆听... 说完请暂停 2 秒")

    results = ""
    while True:
        print(".")
        data = stream.read(4000, exception_on_overflow=False)
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            results = result.get("text", "")
            break

    stream.stop_stream()
    stream.close()
    p.terminate()

    if results:
        print(f"🗣️ 你说：{results}")
    else:
        print("❌ 没有识别到内容")

    return results

listen_speech_lis()
