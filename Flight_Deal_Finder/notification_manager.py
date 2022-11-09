from os import environ
from twilio.rest import Client

# ------------------------------- CONSTANTS ---------------------------------- #
TWILIO_NUM = "[YOUR_TWILIO_NUMBER]"
RECEIVING_NUM = "[RECEIVING NUMBER]"

# ------------------------------- TWILIO DATA -------------------------------- #
account_sid = environ['TWILIO_ACCOUNT_SID'] = "[YOUR ACCOUNT SID]"
auth_token = environ['TWILIO_AUTH_TOKEN'] = "[YOUR AUTH TOKEN]"
client = Client(account_sid, auth_token)


class NotificationManager:
    def __init__(self, data):
        self.data = data

    def send_msgs(self):
        for sms_msg in self.data:
            message = client.messages \
                .create(
                body=sms_msg,
                from_=TWILIO_NUM,
                to=RECEIVING_NUM,
            )
            print(message.status)
