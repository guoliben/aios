import torch
from diffusers import DiffusionPipeline
from diffusers.utils import export_to_video
import numpy as np
import os

# 确保你已登录 Hugging Face（或者使用 token）
# huggingface-cli login

# ✅ 使用小模型：zeroscope_v2_384x256（可在 Mac 上运行）
model_id = "cerspense/zeroscope_v2_384x256"

# 加载模型（dtype 可以是 float32 避免 Half 报错）
pipe = DiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float32,
)

pipe.to("cpu")  # Mac 用 CPU 运行，M 系列支持 MPS 可改为 pipe.to("mps")

# ✅ 文本提示
prompt = "a cat riding a bicycle on a sunny beach"

# ✅ 推理
video_frames = pipe(prompt, num_inference_steps=25).frames  # 默认生成 16 帧

# ✅ 转换 PIL → numpy（以便 export_to_video）
video_frames = [np.array(f) for f in video_frames]

# ✅ 保存为 MP4 视频
video_path = export_to_video(video_frames, output_video_path="output_mac.mp4", fps=8)

print(f"视频已保存: {video_path}")
