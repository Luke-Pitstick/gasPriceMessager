# GasReporter
This bot gets gas prices from a specified zipcode scrapped from gasbuddy and then sends them to your phone.
# Requirements
- poetry
- python3
# Installation
in the folder run

`poetry install`

than create a .env file with the follwing format

```
ACCOUNT_SID = [twilio account sid]
AUTH_TOKEN = [twilio account auth token]
NUMBER = [twilio number]
```

then run

`poetry run python main.py`