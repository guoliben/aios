from TTS.api import TTS

# 初始化模型（首次会自动下载）
tts = TTS(model_name="tts_models/zh-CN/baker/tacotron2-DDC", progress_bar=True)

# 合成语音并保存为文件
tts.tts_to_file(text="你好，这是一个测试。", file_path="output.wav")
