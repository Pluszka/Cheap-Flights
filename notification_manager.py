import os
from twilio.rest import Client


class NotificationManager:

    def send_alert(self, data):
        client = Client(os.environ.get('account_sid'), os.environ.get('auth_token'))
        message = client.messages \
            .create(
            body=f"Low price alert!\n️ Fly to {data.destination}-{data.destination_airport} from"
                 f"{data.start}-{data.start_airport} for only £{data.price}. Date: {data.start_date} to {data.end_date}",
            from_='+18126339019',
            to=os.environ.get('my_phone')
        )
        print(message.status)
