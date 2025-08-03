from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

# 使用视频理解 pipeline
pipe = pipeline(
    task=Tasks.video_captioning,  # 若支持视频文字理解或类似任务名
    model='Qwen/Qwen2.5‑Omni‑7B'
)

# 视频路径输入
result = pipe({'video_path': 'your_video.mp4'})
print("自动描述:", result.get('caption', result))
