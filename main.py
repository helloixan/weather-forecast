import requests
from twilio.rest import Client

# twilio_pw = "felixan123$jovrkpqwt"
# api_key = "a7396f43aa4b7695611a12da30dc4e16"
# account_sid = 'AC1bbc76e28f5f1234b938d44b8d17c869'
# auth_token = 'fb118b82126c66bb2ab4392ddc8815ee'

#-----twilio-------#
account_sid = "AC7c357bb2c70d78979800071781270f39"
auth_token = "0549b71f9a1e07f77368c2e0bac53485"

OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/onecall'
api_key = "69f04e4613056b159c2761a9d9e664d2"

parameters = {
    'lat': -6.974028,
    'lon': 107.630531,
    'appid': api_key,
    'exclude': "current,minutely,daily"
}



response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data['hourly'][:12]

will_rain = False

for hour_data in weather_slice :
    weather_id = hour_data["weather"][0]["id"]
    if weather_id < 700 :
        will_rain = True

if will_rain :
    client = Client(account_sid, auth_token)

    message = client.messages \
                .create(
                    body="it's going rain today, bring an umbrella.",
                    from_='+12057362627',
                    to='+6285656819624'
                )

    print(message.status)