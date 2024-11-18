


#LLM access login 
#web_token = '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'
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers import pipeline
import torch


model_id = "meta-llama/Meta-Llama-Guard-2-8B"
device = "cpu"
task = "text-generation"


pipe = pipeline(
    task=task,
    model=model_id,
    device=device
    )



user_input  = ""
pipe(user_input , max_length = 100)
generate_text = user_input[0]['generated :']
format_output = f"user: \"{user_input}\"\nsystem: \"{generate_text}\""
 


print(format_output)