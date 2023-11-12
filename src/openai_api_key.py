import openai
import os
from dotenv import load_dotenv
from openai import OpenAI
# Load API key from environment variable
load_dotenv()
 

client = OpenAI(os.environ("OPENAI_API_KEY"))

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ]
)
print(response)
