import openai
from datetime import date
from datetime import datetime

openai.api_key = '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'

# get current date and time
now = datetime.now()
DATE = date.today()
TIME = now.strftime("%H:%M:%S")

regex_string = '(?<="content": ")(.*)(?=")'

def response(command):
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages = [{"role": "system", "content" : f"You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible and in as few words as possible.\nKnowledge cutoff: 2021-09-01\nCurrent date: {DATE}\nCurrent time: {TIME}"},
  {"role": "user", "content" : "How are you?"},
  {"role": "assistant", "content" : "I am doing well"},
  {"role": "user", "content" : "what is the time"}]
  )
  
  generated_text = str(response)
  start_index = generated_text.find('"content": "') + len('"content": "')
  end_index = generated_text.find('"', start_index)

  content_string = generated_text[start_index:end_index]
  print(content_string)
