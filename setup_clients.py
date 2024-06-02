# setup_clients.py
import os
from dotenv import load_dotenv
from openai import OpenAI
from twilio.rest import Client

def setup_clients():
    # Load environment variables from .env file
    load_dotenv()

    openAI_client = OpenAI(
        api_key=os.environ.get('OPENAI_API_KEY'),
    )

    twilio_account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    twilio_auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    twilio_phone_number = os.environ.get('TWILIO_PHONE_NUMBER')
    my_phone_number = os.environ.get('MY_PHONE_NUMBER')
    twilio_client = Client(twilio_account_sid, twilio_auth_token)
    
    return openAI_client, twilio_client, twilio_phone_number, my_phone_number
