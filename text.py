from transformers import pipeline
from transformers import AutoTokenizer

import torch
tokenizer = AutoTokenizer.from_pretrained('google-bert/bert-base-cased')
encode_input = tokenizer("Do not meddle in the affairs of wizards, for they are subtle and quick to anger")
device = torch.device('cpu')
print(encode_input)
