import requests

api_key = "3ff0f655c9c8fa45cea3e797dfe4f821"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

print("\nWeather Information")
print("-----------------------")

if "main" in data:
    print("City:", city)
    print("Temperature:", data["main"]["temp"], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Wind Speed:", data["wind"]["speed"], "m/s")
    print("Condition:", data["weather"][0]["description"])
else:
    print("City not found or API error")