# -*- coding: utf-8 -*-
"""Day-54

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rMByzyh_yAxDIKVPxfyOXVi3jR1PdHTF
"""

from transformers import BertTokenizer

def tokenize_sentence(sentence):
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    tokens = tokenizer.tokenize(sentence)
    token_ids = tokenizer.convert_tokens_to_ids(tokens)

    return tokens, token_ids
sentence = "Transformers are revolutionizing NLP."
tokens, token_ids = tokenize_sentence(sentence)

print("Tokens:", tokens)
print("Token IDs:", token_ids)

