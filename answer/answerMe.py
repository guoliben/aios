from transformers import pipeline

chat = pipeline("text-generation", model="distilgpt2")
while True:
    inp = input("你说：")
    result = chat(inp, max_length=100, do_sample=True, top_k=50)[0]['generated_text']
    print("回复：", result[len(inp):].strip())
