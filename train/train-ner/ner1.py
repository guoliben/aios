# from transformers import AutoTokenizer, AutoModelForMaskedLM
#
# tokenizer = AutoTokenizer.from_pretrained("bert-base-chinese")
#
# model = AutoModelForMaskedLM.from_pretrained("bert-base-chinese")


from transformers import BertForTokenClassification, BertTokenizer
from transformers import pipeline

model = BertForTokenClassification.from_pretrained("ckiplab/bert-base-chinese-ner")
tokenizer = BertTokenizer.from_pretrained("ckiplab/bert-base-chinese-ner")

ner = pipeline("ner", model=model, tokenizer=tokenizer)
print(ner("马云在杭州创办了阿里巴巴公司"))