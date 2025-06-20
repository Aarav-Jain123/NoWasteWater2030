# from transformers import pipeline
# import torch
import pdfplumber
# from transformers import AutoTokenizer, AutoModelForCausalLM

def extract_text_from_pdf(file_path):
    full_text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            full_text += page.extract_text() + "\n"
    return full_text

# pipe = pipeline(
#     "text-generation",
#     model="google/gemma-2-2b-it",
#     model_kwargs={"torch_dtype": torch.bfloat16},
#     device="cpu",  # replace with "mps" to run on a Mac device
# )

pdf_text = extract_text_from_pdf("data/merged.pdf")
# # pdf_text1 = extract_text_from_pdf("data/education_nationalgeographic.pdf")
# # pdf_text2 = extract_text_from_pdf("data/en_wikipedia.pdf")
# # pdf_text3 = extract_text_from_pdf("data/mqdefault.pdf")
# # pdf_text4 = extract_text_from_pdf("data/Why-What-How-of-Water-Crisis-Web.pdf")
# # pdf_text = pdf_text1 + pdf_text2 + pdf_text3 + pdf_text4
pdf_text = pdf_text.replace("\n", " ")
pdf_text = pdf_text.replace("  ", " ")
# # print(pdf_text1)
# # print(pdf_text2)
# # print(pdf_text3)
# # print(pdf_text4)
# print(type(pdf_text))
print('extracting content from pdf done, down to next stage')


# chat = [
#     { "role": "user", "content": f"""You are an expert educator and quiz maker. I will upload a PDF document.
# Your task is to:

# Read the entire PDF thoroughly and understand its content.

# Summarize the key concepts and ideas covered.

# Create a quiz based on the content.
# The quiz should include:

# 5 easy multiple-choice questions (MCQs), here is the pdf: {pdf_text}"""}],


# outputs = pipe(chat, max_new_tokens=40960)
# assistant_response = outputs[0]["generated_text"][-1]["content"].strip()
# print(assistant_response)
# # # Okay, let's take a look! 
# # # Based on the image, the animal on the candy is a **turtle**. 
# # # You can see the shell shape and the head and legs.

# # To run this code you need to install the following dependencies:
# # pip install google-genai

# # import base64
# # import os
# # from google import genai
# # from google.genai import types


# # def generate():
# #     client = genai.Client(
# #         api_key=os.environ.get("GEMINI_API_KEY"),
# #     )

# #     model = "gemini-2.5-pro"
# #     contents = [
# #         types.Content(
# #             role="user",
# #             parts=[
# #                 types.Part.from_text(text=pdf_text),
# #             ],
# #         ),
# #     ]
# #     generate_content_config = types.GenerateContentConfig(
# #         thinking_config = types.ThinkingConfig(
# #             thinking_budget=-1,
# #         ),
# #         response_mime_type="text/plain",
# #         system_instruction=[
# #             types.Part.from_text(text="""Your task is to:

# # Read the entire PDF thoroughly and understand its content.

# # Summarize the key concepts and ideas covered.

# # Create a quiz based on the content.
# # The quiz should include:

# # 5 easy multiple-choice questions (MCQs)"""),
# #         ],
# #     )

# #     for chunk in client.models.generate_content_stream(
# #         model=model,
# #         contents=contents,
# #         config=generate_content_config,
# #     ):
# #         print(chunk.text, end="")

# # if __name__ == "__main__":
# #     generate()





# # import os
# # import google.generativeai as genai
# # from dotenv import load_dotenv
# # load_dotenv()

# # genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


# # generation_config = {
# #   "temperature": 0,
# #   "top_p": 0.95,
# #   "top_k": 64,
# #   "max_output_tokens": 9000,
# #   "response_mime_type": "text/plain", # application/json
# # }

# # model = genai.GenerativeModel(
# #   model_name="gemini-1.5-pro",
# #   generation_config=generation_config,
# #   system_instruction="""Your task is to:

# # Read the entire PDF thoroughly and understand its content.

# # Summarize the key concepts and ideas covered.

# # Create a quiz based on the content.
# # The quiz should include:

# # 5 easy multiple-choice questions (MCQs)
# # here is the pdf:
# # """)


# # def pull_answer(prompt):
# #     history = []

# #     chat_session = model.start_chat(
# # history=history
# # )
# #     response = chat_session.send_message(prompt)

# #     model_res = f'''{response.text}'''

# #     history.append(model_res)

# #     return model_res 

# # if __name__ == "__main__":
# #     pull_answer(pdf_text)

from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

tokenizer = AutoTokenizer.from_pretrained("google/gemma-2b-it")
model = AutoModelForCausalLM.from_pretrained("google/gemma-2b")

prompt = f"""You are an expert educator and quiz maker. I will upload a PDF document.
Your task is to:

Read the entire PDF thoroughly and understand its content.

Summarize the key concepts and ideas covered.

Create a quiz based on the content.
The quiz should include:

50 easy multiple-choice questions (MCQs) along with 4 options with 1 correct for each MCQ and 10 facts on water, climate change and water scarcity in africa, here is the pdf: {pdf_text}"""

inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=2048)

# Adjust max_new_tokens depending on output type
try:
    output = model.generate(**inputs, max_new_tokens=100)
    output2 = tokenizer.decode(output[0], skip_special_tokens=True)
    print(f'output2: {output2}')
    with open('hi.txt', 'w') as f:
        f.write(output2)
    # with open('hiw2.txt', 'a') as f:
    #     f.write(output2)
    # with open('hi.txt', 'r') as f:
    #     f.write(output2)
except Exception as e:
    with open("output.jsonl", "a") as f:
        f.write(json.dumps(output) + "\n")
    with open("output.jsonl", "a") as f:
        f.write(json.dumps(output2) + "\n")
    with open("output.jsonl", "w") as f:
        f.write(json.dumps(output2) + "\n")
    with open("output.jsonl", "w") as f:
        f.write(json.dumps(output) + "\n")