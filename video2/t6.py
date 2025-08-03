import torch
import numpy as np
from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler
from diffusers.utils import export_to_video

# 加载模型（你用了 fp16，但是 to("cpu") 不支持半精度，会报错）
# 改为 float32 全精度，或用 CUDA
pipe = DiffusionPipeline.from_pretrained(
    #"damo-vilab/text-to-video-ms-1.7b", 
    "cerspense/zeroscope_v2_384x256",
    torch_dtype=torch.float32,  # 要和设备匹配
).to("mps")  # 若有GPU，建议用 "cuda"

# 更换 scheduler
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)

# 文本生成视频
prompt = "Spiderman is surfing"
output = pipe(prompt, num_inference_steps=25)
video_frames = output.frames  # List of numpy arrays with shape [1, H, W, C]

# ✅ 修复：移除 batch 维度 + 转 uint8
processed_frames = []
for frame in video_frames:
    if isinstance(frame, torch.Tensor):
        frame = frame.detach().cpu().numpy()
    if frame.shape[0] == 1:  # shape: [1, H, W, C]
        frame = frame[0]     # -> [H, W, C]
    if frame.dtype != np.uint8:
        frame = (frame * 255).clip(0, 255).astype(np.uint8)
    processed_frames.append(frame)

# 保存为视频
video_path = export_to_video(processed_frames, output_video_path="output.mp4", fps=8)
print(f"导出视频路径: {video_path}")
