import os
from twilio.rest import Client
from dotenv import load_dotenv
from util.GasScraper import GasScraper

load_dotenv("../.env")


def create_message(bot):
    lowest = bot.get_lowest_price()
    station = list(lowest.keys())[0]
    data = lowest[station]
    price = data["price"]
    address = data["address"]
    address_link = data["address_link"]
    message = f"The cheapest gas is at {station} at ${price}\n\nThe address is {address}\n{address_link}"

    return message


def send_message(messager, message, from_number, to_number):
    message = messager.messages.create(body=message, from_=from_number, to=to_number)

zipcode = 78726


scraper = GasScraper(zipcode)

message = create_message(scraper)

account_sid = os.environ["ACCOUNT_SID"]
auth_token = os.environ["AUTH_TOKEN"]
number = os.environ["NUMBER"]
client = Client(account_sid, auth_token)

send_message(client, message, number, "+15127014145")


# When I make the loop make sure I put in time.sleep() so it doesn't rate limit me.


