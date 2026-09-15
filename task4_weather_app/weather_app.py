import requests

city = input("Write city name: ")
url = f"https://wttr.in/{city}?format=j1"

try:
    response = requests.get(url, verify=False)
    data = response.json()

    temperature = data["current_condition"][0]["temp_C"]
    description = data["current_condition"][0]["weatherDesc"][0]["value"]

    print(f"Weather in {city}: {temperature}°C, {description}")
except Exception:
    print("Could not get weather data. Please check the city name or your internet connection.")