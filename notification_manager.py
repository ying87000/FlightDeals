import smtplib
import requests
from twilio.rest import Client

MY_EMAIL = ""
MY_EMAIL_PASSWORD = ""
PHONE_NUM = ""

class NotificationManager:
    """This class is responsible for sending notifications with the deal flight details."""
    def __init__(self):
        self.account_sid = os.environ['Twilio Account Sid']
        self.auth_token = os.environ['Twilio Auth Token']
        self.client = Client(self.account_sid, self.auth_token)
        self.gsheet_api = os.environ['Google Sheet API']
        self.gsheet_data = requests.get(self.gsheet_api).json()
        self.my_email = MY_EMAIL
        self.password = MY_EMAIL_PASSWORD

    def send_msg(self, msg_body):
        message = self.client.messages.create(
          from_='', #Virtuo Phone Number generated from Twilio
          body=msg_body,
          to=PHONE_NUM
        )
        print(message.sid)

    def send_email(self, to_email,first_name, last_name, msg_body):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.password)
            connection.sendmail(from_addr=self.my_email,
                                to_addrs= to_email,
                                msg=f"Subject: Low Price Alert!\n\n\nDear {first_name} {last_name},\n{msg_body}")

