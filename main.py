import requests
import pyttsx3 as speaker

engine = speaker.init()


api_key = "d8b9c8b8c3254a278d2a6b361f0e157a"
city = "Hamburg"
country_code = "DE"
url = f'https://api.weatherbit.io/v2.0/current?city={city}&country={country_code}&key={api_key}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    weather_data = data['data'][0]

    city_name = weather_data['city_name']
    temperature = weather_data['temp']
    weather_info = weather_data['weather']['description']

    engine.say(f"In {city_name} hat es im Moment {temperature}")
    engine.runAndWait()