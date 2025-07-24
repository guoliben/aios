from transformers import ViTForImageClassification, ViTImageProcessor
from PIL import Image
import torch

# 加载微调后的模型和处理器
model = ViTForImageClassification.from_pretrained("./vit_finetune")
processor = ViTImageProcessor.from_pretrained("./vit_finetune")

# 推理函数
def predict(image_path):
    image = Image.open(image_path).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")
    outputs = model(**inputs)
    pred = outputs.logits.argmax(dim=1).item()
    return pred

# 使用推理函数
img_path = "IMG_0042.jpg"  # 替换为你的测试图片
pred = predict(img_path)
if pred == 0:
    print("✅ 是目标椅子")
else:
    print("❌ 不是目标椅子")