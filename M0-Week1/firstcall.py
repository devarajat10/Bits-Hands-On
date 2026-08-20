import os as os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key= os.getenv('OPEN_AI_KEY'))

response = client.chat.completions.create(
    model='gpt-4.1-mini',
    messages=[
        {'role':"system", 'content':"You are a helpful assistant"},
        {'role':"user", 'content':"What is Gen AI ?"},
    ],
    temperature= 0.7,
    max_tokens=200
)

print(response) 