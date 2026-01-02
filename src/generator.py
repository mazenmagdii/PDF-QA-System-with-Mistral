from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def load_llm():
    model_name="mistralai/Mistral-Nemo-Instruct-2407"
    tokenizer=AutoTokenizer.from_pretrained(model_name)
    model=AutoModelForCausalLM.from_pretrained(model_name,
                                            torch_dtype=torch.float16,
                                            device_map="auto")
    return tokenizer,model

def generate_text(prompt, model, tokenizer, max_length=200, num_return_sequences=1):
    inputs=tokenizer(prompt, return_tensors="pt")
    outputs=model.generate(
        **inputs,
        max_length=max_length,
        num_return_sequences=num_return_sequences,
        do_sample=True,
        top_k=50,
        top_p=0.9,
        temperature=0.2
    )
    return [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
