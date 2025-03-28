import json
import requests

API_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Lake%20Country%2C%20Kelowna/today?unitGroup=metric&key=9YZXSLJYPJGRMQDFKJW5G2QMQ&contentType=json"
filename = "weatherData.json"


def download_json(api_url):
    r = requests.get(api_url)
    with open(filename, "wb") as f:
        f.write(r.content)

download_json(API_URL)


with open(filename, "r") as file:
    data = json.load(file)

maxTemp = data["days"][0]["tempmax"]
print(maxTemp)