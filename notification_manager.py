import os
from twilio.rest import Client
import smtplib

MY_EMAIL = os.environ.get('MY_EMAIL')
MY_PASSWORD = os.environ.get('EMAIL_PASSWORD')
txt: str
class NotificationManager:

    def send_alert(self):
        global txt
        client = Client(os.environ.get('account_sid'), os.environ.get('auth_token'))
        message = client.messages \
            .create(
            body= txt,
            from_='+18126339019',
            to=os.environ.get('my_phone')
        )
        print(message.status)

    def send_email(self, users_emails):
        global txt
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for user in users_emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=user['email'],
                    msg=f'Subject:Cheap Fly Alert\n\n{txt}'.encode('utf-8')
                )

    def create_message(self, data):
        global txt
        link = f"https://www.google.co.uk/flights?hl=en#flt={data.start_airport}.{data.destination_airport}.\
{data.start_date}*{data.destination_airport}.{data.start_airport}.{data.end_date}"
        txt = f"Low price alert!\n️ Fly to {data.destination}-{data.destination_airport} from \
                {data.start}-{data.start_airport} for only U+00A3{data.price}.\
                Date: {data.start_date} to {data.end_date}\n\n{link}"
        if data.stop_overs > 0:
            txt = f"{txt}\n Stop over in {data.via_city}"
