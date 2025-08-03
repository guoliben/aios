# from TTS.utils.manage import ModelManager
#
# manager = ModelManager()
# path = manager.download_model("tts_models/zh-CN/baker/tacotron2-DDC-GST")
# # print(f"模型已下载到: {path}")


# from TTS.api import TTS
#
# tts = TTS(model_name="tts_models/zh-CN/baker/tacotron2-DDC-GST")
# tts.tts_to_file(text="你好，欢迎使用语音合成。", file_path="output.wav")

# tts 路径： /Users/ben/Library/Application\ Support/tts/tts_models-

from TTS.api import TTS

# tts = TTS(model_name="/Users/ben/Library/Application Support/tts/tts_models/zh-CN/baker/tacotron2-DDC-GST")
tts = TTS(model_name="tts_models/zh-CN/baker/tacotron2-DDC-GST")
# tts = TTS(model_name="tts_models--zh-CN--baker--tacotron2-DDC-GST")
tts.tts_to_file(text="你好，欢迎使用语音合成。", file_path="output.wav")