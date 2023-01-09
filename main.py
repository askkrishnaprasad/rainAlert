import requests

API_KEY = "f1aba80eab07b8645b4a89aa3d8f2881"
MY_LAT = 43.761539
MY_LOG = -79.411079

parameters = {
    "lat": MY_LAT,
    "lon": MY_LOG,
    "exclude": "current,minutely,daily",
    "appid": API_KEY,
}

response = requests.get(url="https://api.openweathermap.org/data/3.0/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_data = weather_data["hourly"][:12]

will_rain = False

for data in weather_data:
    condition_code = int(data["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True

if will_rain:
    print("It will rain bring an umbrella.!")
