from transformers import AlbertTokenizer, AlbertForSequenceClassification
import torch

model_path = "albert_log_output/checkpoint-1"  # 训练完成后路径
tokenizer = AlbertTokenizer.from_pretrained(model_path)
model = AlbertForSequenceClassification.from_pretrained(model_path)


for i in range(10):
    log_text = "Jul 26 12:34:56 myhost sshd[1234]: Accepted password for user from 10.0.0.1"
    inputs = tokenizer(log_text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        logits = model(**inputs).logits
        predicted_class = torch.argmax(logits, dim=1).item()

    print("Predicted class:", predicted_class)


# from transformers import AlbertTokenizer, AlbertForSequenceClassification
# import torch
#
# # model_name = "albert-tiny-v2"  # 或 albert-small-v2、albert-base-v2
# model_name = "albert-base-v2"  # 或 albert-small-v2、albert-base-v2
# tokenizer = AlbertTokenizer.from_pretrained(model_name)
# model = AlbertForSequenceClassification.from_pretrained(model_name, num_labels=5)  # 你有几类就填几
#
# # 假设你要预测下一条日志类型
# log_text = "Jul 26 12:34:56 myhost sshd[1234]: Accepted password for user from 10.0.0.1"
#
# inputs = tokenizer(log_text, return_tensors="pt", truncation=True, padding=True)
# with torch.no_grad():
#     logits = model(**inputs).logits
#     predicted_class = torch.argmax(logits, dim=1).item()
#
# print("Predicted class:", predicted_class)
