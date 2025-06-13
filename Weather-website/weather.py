from dotenv import load_dotenv
import requests
import os

load_dotenv()

def get_current_weather(city):
    request_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('OPENWEATHER_API_KEY')}&units=metric"
    weather_data = requests.get(request_url).json()
    return weather_data

if __name__ == "__main__":
    print("\n*** Get Current Weather Conditions ***\n")
    city = input("\nPlease enter a city name: ")
    weather_data = get_current_weather(city)
    print("\n")
    print(weather_data)
