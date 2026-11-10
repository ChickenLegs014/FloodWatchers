'''
Authors     : Aaron Sapp & Warren Nixon
Date        : Nov. 10, 2026
Course      : CSCI Special Topics: Problem Solving
Assignment  : Project Phase 3: Development - Part 1 (Core Logic)
Module      : api.py
Description : Extracts and creates data from USGS into a JSON file.
'''

# Libraries and frameworks
import requests, json

# Station ID (Tularosa)
station_id = '08481500'

# Build the request URL for instantaneous values in JSON format
# parameterCd '00065' = Gage Height, '00060' = Streamflow
url = f'https://waterservices.usgs.gov/nwis/iv/?format=json&sites={station_id}&parameterCd=00065,00060'

# Execute HTTP GET request
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # Drill down into JSON strucutre to extract time series arrays
    time_series = data['value']['timeSeries']

    # Iterates through 'time_series'
    for data in time_series:
        var_descriptions = data['variable']['variableDescription']
        latest_record = data['values'][0]
        value = latest_record['value'][0]['value']
        timestamp = latest_record['value'][0]['dateTime']

        print(f"Metric: {var_descriptions}")
        print(f"Latest Value: {value}")
        print(f"Recorded At: {timestamp}\n")

    with open("river_data.json", "w") as file:
        json.dump(data, file, indent = 4)

    print("Data saved successfully to river_data.json!")

else:
    print(f"Failed to fetch data. Status code: {response.status_code}")

