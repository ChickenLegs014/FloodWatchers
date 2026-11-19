# Libraries and frameworks
import requests
import json

# Set coordinates (Alamogordo)
latitude = 32.2800
longitude = -106.7500

# Set url
url = f"https://api.weather.gov/alerts/active/area/NM"

# Downloads data from url
response = requests.get(url)

# Extracts data from url
data = response.json()

# Export data into a json file
with open("data", "w") as file:
    json.dump(data, file, indent = 4)

for alert in data.get("features"):
    props = alert["properties"]
    print(f"[{props['severity']}] {props['event']}: {props['headline']}")