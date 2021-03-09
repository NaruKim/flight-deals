from twilio.rest import Client

TWILIO_SID = "AC5fb6a8d0670c958f4c6d3e9f200998e0"
TWILIO_AUTH_TOKEN = ""

class NotificationManager:
    def texting(self, text_body):
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=text_body,
            from_="+15103302089",
            to=""
        )