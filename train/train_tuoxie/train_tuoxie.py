from transformers import ViTForImageClassification, ViTFeatureExtractor, TrainingArguments, Trainer
from datasets import load_dataset
from torchvision import transforms
from PIL import Image
import torch
import os

# 加载预训练模型
model = ViTForImageClassification.from_pretrained(
    "google/vit-base-patch16-224",
    num_labels=2,
    ignore_mismatched_sizes=True
)

# 图像预处理
feature_extractor = ViTFeatureExtractor.from_pretrained("google/vit-base-patch16-224")
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=feature_extractor.image_mean, std=feature_extractor.image_std),
])

# 自定义 PyTorch Dataset
class CustomImageDataset(torch.utils.data.Dataset):
    def __init__(self, image_folder, transform):
        self.image_folder = image_folder
        self.transform = transform
        self.samples = []
        for label, cls in enumerate(sorted(os.listdir(image_folder))):
            cls_path = os.path.join(image_folder, cls)
            for f in os.listdir(cls_path):
                self.samples.append((os.path.join(cls_path, f), label))

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        image_path, label = self.samples[idx]
        image = Image.open(image_path).convert("RGB")
        return {"pixel_values": self.transform(image), "labels": label}

# 加载数据
train_dataset = CustomImageDataset("dataset/train", transform)
val_dataset = CustomImageDataset("dataset/val", transform)

# 训练配置
training_args = TrainingArguments(
    output_dir="./vit_finetune",
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    evaluation_strategy="epoch",
    save_strategy="epoch",
    num_train_epochs=5,
    logging_dir="./logs",
)

# 开始训练
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
)

# 训练模型
trainer.train()

# ✅ 保存微调后的模型结构和权重（含 config.json）
trainer.save_model("./vit_finetune")

# ✅ 保存图像预处理器（含 mean/std/size 等）
feature_extractor.save_pretrained("./vit_finetune")