from transformers import ViTForImageClassification, ViTFeatureExtractor, TrainingArguments, Trainer
from torchvision import transforms
from PIL import Image
import torch
import os

# ✅ 自动选择设备：优先用 MPS，其次 CUDA，再次 CPU
if torch.backends.mps.is_available():
    device = torch.device("mps")
elif torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

print(f"Using device: {device}")

# ✅ 加载预训练模型并迁移到设备
model = ViTForImageClassification.from_pretrained(
    "facebook/deit-tiny-patch16-224",
    num_labels=2,
    ignore_mismatched_sizes=True
)
model.to(device)

# ✅ 图像预处理配置
feature_extractor = ViTFeatureExtractor.from_pretrained("facebook/deit-tiny-patch16-224")
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=feature_extractor.image_mean, std=feature_extractor.image_std),
])

# ✅ 自定义 PyTorch Dataset
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
        return {
            "pixel_values": self.transform(image),
            "labels": torch.tensor(label, dtype=torch.long),
        }

# ✅ 加载数据集
train_dataset = CustomImageDataset("dataset/train", transform)
val_dataset = CustomImageDataset("dataset/val", transform)

# ✅ 自定义 Trainer 中的数据 collate_fn（必要！否则 MPS 可能报错）
def collate_fn(batch):
    pixel_values = torch.stack([item["pixel_values"] for item in batch])
    labels = torch.tensor([item["labels"] for item in batch])
    return {"pixel_values": pixel_values, "labels": labels}

# ✅ 训练配置
training_args = TrainingArguments(
    output_dir="./vit_finetune",
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    evaluation_strategy="epoch",
    save_strategy="epoch",
    num_train_epochs=5,
    logging_dir="./logs",
    remove_unused_columns=False,  # 必须显式关闭，防止pixel_values被移除
    dataloader_pin_memory=False,  # MPS 不支持 pinned memory
)

# ✅ 初始化 Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    data_collator=collate_fn,
)

# ✅ 开始训练
trainer.train()

# ✅ 保存模型和特征提取器
trainer.save_model("./vit_finetune")
feature_extractor.save_pretrained("./vit_finetune")
