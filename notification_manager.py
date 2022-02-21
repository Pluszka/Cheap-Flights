import os
from twilio.rest import Client


class NotificationManager:

    def send_alert(self, data):
        text = f"Low price alert!\n️ Fly to {data.destination}-{data.destination_airport} from"
        f"{data.start}-{data.start_airport} for only £{data.price}. Date: {data.start_date} to {data.end_date}"
        if data.stop_overs > 0:
            text = f"{text}\n Stop over in {data.via_city}"
        client = Client(os.environ.get('account_sid'), os.environ.get('auth_token'))
        message = client.messages \
            .create(
            body= text,
            from_='+18126339019',
            to=os.environ.get('my_phone')
        )
        print(message.status)
