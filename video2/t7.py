import torch
from diffusers import DiffusionPipeline
from diffusers.utils import export_to_video

# 设置为 MPS 后端（苹果芯片专用）
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")

# 加载小模型
pipe = DiffusionPipeline.from_pretrained(
    "cerspense/zeroscope_v2_30x448x256",
    #"cerspense/zeroscope_v2_384x256",
    torch_dtype=torch.float32  # MPS 目前不稳定支持 float16，建议 float32
)# .to(device)

# 生成视频帧
prompt = "a fox running through a snowy forest, cinematic"
video_frames = pipe(prompt, num_inference_steps=20).frames
video_frames = [np.array(frame) for frame in video_frames]

# 导出为视频
video_path = export_to_video(video_frames, output_video_path="mac_output.mp4", fps=8)

print("✅ 视频生成完成，文件路径:", video_path)
