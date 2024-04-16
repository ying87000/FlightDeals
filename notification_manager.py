import smtplib
import requests
from twilio.rest import Client


class NotificationManager:
    """This class is responsible for sending notifications with the deal flight details."""
    def __init__(self):
        self.account_sid = 'AC4b5877a2ed5b127afe734f030582fe34'
        self.auth_token = 'd7bdee3c54e82f59a8dab755215142ca'
        self.client = Client(self.account_sid, self.auth_token)
        self.gsheet_api = "https://api.sheety.co/46eaace6c0923e882fbe2f5e8f3bf9bc/flightDeals/users"
        self.gsheet_data = requests.get(self.gsheet_api).json()
        self.my_email = "gtbio.albee1@gmail.com"
        self.password = "pugq vuwh sbnv qbie"

    def send_msg(self, msg_body):
        message = self.client.messages.create(
          from_='+15167569013',
          body=msg_body,
          to='+886905060485'
        )
        print(message.sid)

    def send_email(self, to_email,first_name, last_name, msg_body):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.password)
            connection.sendmail(from_addr=self.my_email,
                                to_addrs= to_email,
                                msg=f"Subject: Low Price Alert!\n\n\nDear {first_name} {last_name},\n{msg_body}")

