# you need to pip install schedule and pip install requests

# I add phone_number variable to some privacy reasons (you need to give the number to this variable)
from phonenumber import phone_number
import requests
import schedule
import time
#I use the 'key' for using trail version
def send_message():
    resp=requests.post('https://textbelt.com/text', {
        'phone': phone_number,
        'message': 'hi, how are you today',
        'key': 'textbelt',

    })
    print(resp.json())

schedule.every().day.at('09:00').do(send_message)