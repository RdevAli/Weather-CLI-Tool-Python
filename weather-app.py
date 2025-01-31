import os
from dotenv import load_dotenv, dotenv_values
import requests

load_dotenv()

key = os.getenv("MYKEY")
base_url= "https://api.openweathermap.org/data/2.5"
user_input= input("Enter City: ")
weather_data = requests.get(f"{base_url}/weather?q={user_input}&units=metric&appid={key}")
weather = weather_data.json()['weather'][0]['main']
temp = weather_data.json()['main']['temp']
humidity = weather_data.json()['main']['humidity']
print(f"Current Weather at {user_input} is {weather}, with current temperature of {temp} Celcius and humidity of {humidity}")
lat= weather_data.json()['coord']['lat']
lon= weather_data.json()['coord']['lon']

forecast_response = requests.get(f"{base_url}/forecast?lat={lat}&lon={lon}&units=metric&appid={key}")
data = forecast_response.json()

if "list" in data:
        forecast_data = {}

        for entry in data["list"]:
            date = entry["dt_txt"].split()[0]
            temp = entry["main"]["temp"]
            weather = entry["weather"][0]["description"].title()
            humidity = entry["main"]["humidity"]
            forecast_data.setdefault(date, []).append((temp, weather, humidity))

        print("The Forecast for next 5 days is: ")
        for date, values in forecast_data.items():
            avg_temp = sum(temp for temp, _, _ in values) / len(values)
            common_weather = max(set(w for _, w, _ in values), key=lambda w: [w for _, x, _ in values].count(w))
            avg_humidity = sum(h for _, _, h in values) / len(values)
            
            print(f"{date}: {avg_temp:.1f}°C, {common_weather}, Humidity: {avg_humidity:.1f}%")

else:  
    print("Error fetching forecast data.")
