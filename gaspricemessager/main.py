import os
from twilio.rest import Client
from dotenv import load_dotenv
from controllers.GasScraper import GasScraper
load_dotenv('../.env')

scrapper = GasScraper()

account_sid = os.environ['ACCOUNT_SID']
auth_token = os.environ['AUTH_TOKEN']
number = os.environ['NUMBER']
client = Client(account_sid, auth_token)

message = client.messages.create(
    body='I\'m watching you',
    from_=number,
    to='+15127014145'
  )

print(message.sid)