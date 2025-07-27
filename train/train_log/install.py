from transformers import AlbertTokenizer, AlbertModel

tokenizer = AlbertTokenizer.from_pretrained("albert/albert-base-v2")
model = AlbertModel.from_pretrained("albert/albert-base-v2")



# from transformers import AlbertTokenizer
#
# tokenizer = AlbertTokenizer.from_pretrained("prajjwal1/albert-tiny", use_auth_token=False)


# from transformers import AlbertTokenizer, AlbertModel
#
# model_name = "prajjwal1/albert-tiny"  # 替换掉错误的 albert-tiny-v2
#
# tokenizer = AlbertTokenizer.from_pretrained(model_name)
# model = AlbertModel.from_pretrained(model_name)




# from transformers import AlbertTokenizer
#
# # tokenizer = AlbertTokenizer.from_pretrained("albert-tiny-v2")
# tokenizer = AlbertTokenizer.from_pretrained("google/albert-base-v2")
# print(tokenizer.tokenize("This is a test log line."))
