import requests
from twilio.rest import Client

#-----twilio-------#
account_sid = "-"
auth_token = "-"

OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/onecall'
api_key = "-"

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
