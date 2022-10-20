import torch
from transformers import GPT2Tokenizer, GPTNeoForCausalLM

if __name__ == '__main__':
    tokenizer = GPT2Tokenizer.from_pretrained("EleutherAI/gpt-neo-1.3B", cache_dir = './gpt2_tok')
    model = GPTNeoForCausalLM.from_pretrained("EleutherAI/gpt-neo-1.3B", cache_dir = './gpt_neo')

    prompt = "a,b,c,d,e,f"
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model(**inputs, labels=inputs["input_ids"])
    loss = outputs.loss
    logits = outputs.logits

    greedy_output = model.generate(input_ids = inputs["input_ids"], max_length=256)

    print(tokenizer.decode(greedy_output[0], skip_special_tokens=True))

    # for fine-tuning alter loss at the final layer.