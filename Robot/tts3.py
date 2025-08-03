from TTS.api import TTS

print("11")
# 本地路径加载模型
tts = TTS(model_path="tts_models/zh-CN/baker/tacotron2-DDC", progress_bar=True)

print("22")
print(tts)
tts.tts_to_file("你好，这是本地模型测试", "test.wav")
