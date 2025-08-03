import whisper

# 加载模型，tiny最小，large最准确，推荐根据设备资源选择
model = whisper.load_model("base")

# 识别文件，默认自动语言检测，也可以指定 language='zh'
result = model.transcribe("../audio/output.mp3", language="zh")

print("识别结果：", result["text"])
