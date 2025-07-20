import os
os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"

from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# model_name = "deepseek-ai/deepseek-coder-1.3b-instruct"
model_name = "deepseek-coder-1.3b-instruct"



tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/deepseek-coder-1.3b-instruct", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    "deepseek-ai/deepseek-coder-1.3b-instruct",
    torch_dtype=torch.float16,
    device_map="auto",
    trust_remote_code=True
)
#
# tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
# model = AutoModelForCausalLM.from_pretrained(
#     model_name,
#     torch_dtype=torch.float16,
#     device_map="auto",  # 会根据 MPS/CPU 自动调度
#     trust_remote_code=True
# )

while True:
    user_input = input("🧑 你：")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("👋 再见！")
        break
    prompt = "你好，请介绍一下你自己。"
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(**inputs, max_new_tokens=128, do_sample=True, temperature=0.7)
    print(tokenizer.decode(outputs[0], skip_special_tokens=True))




'''
import os
os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"

from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_name = "deepseek-ai/deepseek-coder-1.3b-instruct"

print("🚀 模型加载中，请稍候...")

tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map="auto",
    trust_remote_code=True
)

print("✅ 模型已加载，开始对话吧！输入 'exit' 退出。\n")

history = ""

while True:
    user_input = input("🧑 你：")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("👋 再见！")
        break

    # 构造 Prompt（可选：保留历史对话以支持上下文）
    prompt = history + f"\n用户：{user_input}\n助手："

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(
        **inputs,
        max_new_tokens=256,
        do_sample=True,
        temperature=0.7,
        pad_token_id=tokenizer.eos_token_id
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # 截取回答部分（去除 Prompt）
    answer = response[len(prompt):].strip()

    print(f"🤖 助手：{answer}\n")

    # 更新历史记录
    history += f"\n用户：{user_input}\n助手：{answer}"
'''

