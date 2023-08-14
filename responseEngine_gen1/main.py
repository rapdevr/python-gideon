import openai
from datetime import date
from datetime import datetime

openai.api_key = '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'

# get current date and time
now = datetime.now()
DATE = date.today()
TIME = now.strftime("%H:%M:%S")

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages = [{"role": "system", "content" : f"You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible.\nKnowledge cutoff: 2021-09-01\nCurrent date: {DATE}\nCurrent time: {TIME}"},
{"role": "user", "content" : "How are you?"},
{"role": "assistant", "content" : "I am doing well"},
{"role": "user", "content" : "What is the tallest mountain in the world?"}]
)

generated_text = response
print(generated_text)

