import smtplib
import requests
from twilio.rest import Client

USER_DATA_GET_ENDPOINT = "https://api.sheety.co/8aee92b9d053a6a4c35116f530584a6f/copyOfFlightDeals/users"

TWILIO_SID = "AC5fb6a8d0670c958f4c6d3e9f200998e0"
TWILIO_AUTH_TOKEN = ""

EMAIL = ""
TO = ""
PASSWORD = ""

class NotificationManager:
    def texting(self, text_body):
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=text_body,
            from_="+15103302089",
            to=""
        )

    def user_data_email(self):
        self.user_data=[]
        response = requests.get(USER_DATA_GET_ENDPOINT).json()['users']
        for i in response:
            self.user_data.append(i['email'])
        return self.user_data

    def mailing(self, text_body):
        email_list = self.user_data_email()

        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        for i in email_list:
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=i,
                msg=f"subject:Flight\n\n{text_body}",
            )
            print (f"Email to {i} sent")
