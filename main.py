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

def print_data(x):
    with open(weather_json, "r") as file:
        data = json.load(file)

    date = data ["days"][0]["datetime"]
    max_temp = data["days"][0]["tempmax"]
    min_temp = data["days"][0]["tempmin"]
    feelmax_temp = data["days"][0]["feelslikemax"]
    feelmin_temp = data["days"][0]["feelslikemin"]
    print(date)

    if x == "f":
        print(f"Temperature: {min_temp * 9/5 + 32} - {max_temp * 9/5 + 32} °F")
        print(f"Temperature feels like: {feelmin_temp * 9/5 + 32} - {feelmax_temp * 9/5 + 32} °C")
    else:
        print(f"Temperature: {min_temp} - {max_temp} °C")
        print(f"Temperature feels like: {feelmin_temp} - {feelmax_temp} °C")





#Update weather files
while True:
    todays_date = datetime.date.today()

    if todays_date != last_checked_time:
        download_json(API_URL)
        print_data()
        print("Waiting for change...")
        time.sleep(60)

    #main logic here -->
    else:
        print_data(input("f or c: "))
        break 
