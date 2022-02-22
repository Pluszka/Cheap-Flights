from user_data import UserData
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

flight = FlightSearch()
sheet_data = DataManager()
notification = NotificationManager()
emails = UserData()

for country in sheet_data.prices:
    if len(country['iataCode']) == 0:
        country['iataCode'] = flight.get_code(country['city'])

for country in sheet_data.prices:
    today_flight = flight.found_flight(country['iataCode'])
    try:
        current_price = today_flight.price
    except AttributeError:
        pass
    else:
        if country['lowestPrice'] > current_price:
            print('lower')
            notification.create_message(today_flight)
            notification.send_alert()
            notification.send_email(emails)

# print('Let\'s sing up to the flight club!')
# emails.add_user()
# print('Thanks for register to service')
