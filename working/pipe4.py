# from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# model_name = "gpt2"  # replace with "gemma-3b" if released

# # Load tokenizer and model
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")

# # Setup pipeline for text generation
# pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)

# # Prompt and generation
# prompt = "Generate 5 questions on water and its scarcity along with 4 options"
# output = pipe(prompt, max_new_tokens=8192, do_sample=True, temperature=0.7)

# print(output[0]["generated_text"])

import torch
from transformers import pipeline
from huggingface_hub import login
from dotenv import load_dotenv
import os

load_dotenv()

login(os.getenv("HUGGING_FACE_KEY"))

generator = pipeline(
    task="image-text-to-text",
    model="google/gemma-3-4b-pt",
    device=0,
    torch_dtype=torch.bfloat16
)
res = generator(
    "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/pipeline-cat-chonk.jpeg",
    text="<start_of_image> What is shown in this image?"
)

print(res)
