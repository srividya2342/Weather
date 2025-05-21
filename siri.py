import requests
def get_weather(city, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        print(f"🌤️ Weather in {city}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Weather: {data['weather'][0]['description']}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        print("Check Your City Name.😊")

# ---------- USER INPUT ----------
city_name = input("Enter city name: ")
api_key = "42dcaaf93c754944124c105c5698f276"
get_weather(city_name, api_key)
