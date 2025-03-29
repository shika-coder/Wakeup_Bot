import time
import json
import requests
import os
import datetime

API_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Lake%20Country%2C%20Kelowna/today?unitGroup=metric&key=9YZXSLJYPJGRMQDFKJW5G2QMQ&contentType=json"
weather_json = "weatherData.json"
weather_path = "/weatherData.json"

def download_json(api_url):
    if os.path.exists(weather_path):
        os.remove(weather_path)
    
    r = requests.get(api_url)
    with open(weather_json, "wb") as f:
        f.write(r.content)


last_checked_time = datetime.date.today()

download_json(API_URL)

def print_data():
    with open(weather_json, "r") as file:
        data = json.load(file)

    max_temp = data["days"][0]["tempmax"]
    min_temp = data["days"][0]["tempmin"]

    print(f"Temperature: {min_temp} - {max_temp}")






#Update weather files
while True:
    todays_date = datetime.date.today()

    if todays_date != last_checked_time:
        download_json(API_URL)
        print_data()
        print("Waiting for change...")
        time.sleep(60)

    else:
        print_data()
        break 
    