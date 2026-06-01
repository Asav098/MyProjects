import requests
city = input("Enter the city: ")
url = f"https://wttr.in/{city}?format=j1"
response = requests.get(url)
data = response.json()
req = data["current_condition"][0]
temp = req["temp_C"]
humidity = req["humidity"]
description = req["weatherDesc"][0]["value"]
wind = req["windspeedKmph"]
feels_like = req["FeelsLikeC"]
print(f"Weather in {city}")
print(f"The temp is {temp} C")
print(f"Temperature  : {temp}°C")
print(f"Feels like   : {feels_like}°C")
print(f"Description  : {description}")
print(f"Humidity     : {humidity}%")
print(f"Wind speed   : {wind} km/h")