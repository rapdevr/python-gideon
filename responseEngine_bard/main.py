# 03. usage
import bardapi
import bardapi.core
import re

# set your __Secure-1PSID value to key
token='YwgwxdYMcKFTHGTiIOAEUAJZv9ZwYnA7QbizF4gn1y8-_3Lf8H3zdgnzJqIf_79ztrGQBg.'

def request(text):
    # set your input text
    input_text = f"as simply as possible without using any formatting, {text}"

    # Send an API request and get a response.
    response = bardapi.core.Bard(token).get_answer(input_text)
    # isolate the data that I want from the response
    isolated_text = response.get('content',None)
    # print the isolated text
    print(isolated_text)