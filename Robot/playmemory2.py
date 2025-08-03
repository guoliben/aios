import soundfile as sf
import sounddevice as sd
from pyaec import Aec

# 音频参数
frame_size = 256
filter_length = 2048
sample_rate = 16000

# 获取数据
def get_data(path):
    data, sr = sf.read(path, dtype='int16')
    if sr != sample_rate:
        raise ValueError(f"采样率应为 {sample_rate}Hz，但读取为 {sr}Hz")
    if data.ndim == 2:
        data = data[:, 0]  # 取单通道
    return data.tolist()

# 初始化AEC
aec = Aec(frame_size, filter_length, sample_rate)

# 读取录音和回声源数据
echo_buffer = get_data("temp.wav")     # 外放声源
rec_buffer  = get_data("temp2.wav")    # 含回声的录音

# 取最短长度，避免越界
min_len = min(len(echo_buffer), len(rec_buffer))

# 分帧处理
cleaned_output = []
for i in range(0, min_len - frame_size + 1, frame_size):
    echo_frame = echo_buffer[i:i + frame_size]
    rec_frame  = rec_buffer[i:i + frame_size]
    out_frame  = aec.cancel_echo(rec_frame, echo_frame)
    cleaned_output.extend(out_frame)

# 保存去回声结果
sf.write("cleaned.wav", cleaned_output, samplerate=sample_rate, subtype='PCM_16')

# 播放对比
print("播放原始含回声音频")
sd.play(rec_buffer, sample_rate)
sd.wait()

print("播放去回声音频")
sd.play(cleaned_output, sample_rate)
sd.wait()