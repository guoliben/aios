from transformers import AlbertTokenizer, AlbertForSequenceClassification, Trainer, TrainingArguments
from datasets import load_dataset
import torch
import pandas as pd
from sklearn.model_selection import train_test_split

# 读取 CSV 并划分数据集
df = pd.read_csv("log_data.csv")
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

# 保存为 huggingface datasets 格式
train_df.to_csv("train.csv", index=False)
test_df.to_csv("test.csv", index=False)

dataset = load_dataset("csv", data_files={"train": "train.csv", "test": "test.csv"})

# 加载 tokenizer 和模型
model_name = "albert-base-v2"
tokenizer = AlbertTokenizer.from_pretrained(model_name)
model = AlbertForSequenceClassification.from_pretrained(model_name, num_labels=3)  # 改为你的类别数

# Tokenizer函数
def tokenize_function(example):
    return tokenizer(example["text"], truncation=True, padding=True)

tokenized_dataset = dataset.map(tokenize_function, batched=True)

# 设置训练参数
training_args = TrainingArguments(
    output_dir="./albert_log_output",
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=5,
    evaluation_strategy="epoch",
    save_strategy="epoch",
    logging_dir="./logs",
    logging_steps=10,
    load_best_model_at_end=True,
    save_total_limit=1,
)

# 训练器
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"],
    eval_dataset=tokenized_dataset["test"],
    tokenizer=tokenizer,
)

trainer.train()



# from transformers import Trainer, TrainingArguments
#
# training_args = TrainingArguments(
#     output_dir="./log_model",
#     per_device_train_batch_size=32,
#     per_device_eval_batch_size=32,
#     num_train_epochs=3,
#     logging_dir='./logs',
#     evaluation_strategy="steps",
# )
#
# trainer = Trainer(
#     model=model,
#     args=training_args,
#     train_dataset=train_ds,
#     eval_dataset=eval_ds,
#     tokenizer=tokenizer
# )
#
# trainer.train()
