from transformers import AutoTokenizer, AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained(
    #"openbmb/MiniCPM-2B",
    "openbmb/MiniCPM-o-2_6",
    trust_remote_code=True,
    device_map="auto"  # 自动分配GPU/CPU
)
tokenizer = AutoTokenizer.from_pretrained("openbmb/MiniCPM-2B", trust_remote_code=True)

input_text = "中国的首都是哪？"
inputs = tokenizer(input_text, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=64)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
