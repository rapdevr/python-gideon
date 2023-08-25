from bardapi import Bard
import os
import requests

# Set the Bard API key in the environment variable
os.environ['_BARD_API_KEY'] = 'ZwgwxScRR8pBCI2mrLFZhkNCRFHAA7YtkBjT3kpeKsqH7F9Im95Xm2yvBU3LUDTfncC_xQ.'
os.environ['_BARD_API_KEYTS'] = 'sidts-CjIBSAxbGR2iC5nE_6honG0-511heM5mI1Gcnd4L6-bUxE0suOrFEYEOIKomGSbsaqq_ixAA'
os.environ['_BARD_API_KEYCC'] = 'APoG2W8iuefrCkyXymYbW5hVkNdIe0wJHEkIUNpNyw7suxcbjOacx5Vh9XBEGsI7UoZ2NhwEK1s'

# Create a session object using the requests library
session = requests.Session()

# Set the headers for the session
session.headers = {
            "Host": "bard.google.com",
            "X-Same-Domain": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Origin": "https://bard.google.com",
            "Referer": "https://bard.google.com/",
        }

# Set the "__Secure-1PSID" cookie with the Bard API key
session.cookies.set("__Secure-1PSID", os.getenv("_BARD_API_KEY"))
session.cookies.set("__Secure-1PSIDTS", os.getenv("_BARD_API_KEYTS"))
session.cookies.set("__Secure-1PSIDCC", os.getenv("_BARD_API_KEYCC"))
# Create a Bard object with the session and a timeout of 30 seconds
bard = Bard(session=session, timeout=30)

def request(text):
    input_text = f"as simply as possible and without using any formatting, {text}"

    # Send an API request and get a response
    response = bard.get_answer(input_text)['content']
    print(response)
    return(response)