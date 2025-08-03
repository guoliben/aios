#pip install transformers accelerate
#pip install transformers accelerate

from transformers import AutoTokenizer, AutoModelForCausalLM

module_name = "openbmb/MiniCPM-o-2_6"
module_name = "openbmb/MiniCPM4-0.5B"
model = AutoModelForCausalLM.from_pretrained(module_name, device_map="auto", trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained(module_name, trust_remote_code=True)

prompt = "用户: 什么是DPI？\n助手:"
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=128)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))

