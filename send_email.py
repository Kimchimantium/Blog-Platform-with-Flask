import smtplib
from email.mime.text import MIMEText
import json


class Smtp:

    def __init__(self, user_credentials):
        self.user_credentials = user_credentials
        pass

    def send_email(self):
        pass
        user_credentials_str = json.dumps(self.user_credentials, indent=2)
        subject = 'New Message from Flask Practicing Blog'
        body = user_credentials_str
        message = MIMEText(body, 'plain')
        message['Subject'] = subject
        message['From'] = "dukso123@gmail.com"
        message['To'] = "dukso123@gmail.com"
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login('dukso123@gmail.com', 'aiii bwgp facj djmp')
            server.sendmail('dukso123@gmail.com', 'dukso123@gmail.com', message.as_string())
            print('message sent successfully')
        except smtplib.SMTPException as e:
            print(f"Error occured: {e}")
