# Cheap-Flights
App which search for bargin prices of flights
Run add_user.py to add user to database. Then run main.py App will check if you can buy flight ticket by lower price than price you put into google sheet
(use sheety to create api for that database, the same for users) When price is lower app will send emails to users.

!!ATENTION!! You have to first create database with rices and countries. Sheet prices (headers requaierd: City,	IATA Code,	Lowest Price) and users(headers requaierd: First Name,	Last Name,	Email)

APP inspired by https://jacksflightclub.com/eu

API used:
https://www.twilio.com/docs/sms
https://partners.kiwi.com/
https://sheety.co/
