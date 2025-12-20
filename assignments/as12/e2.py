#https://openweathermap.org/api
#default key: c90a5414b5655205674b32ff578aad62
import requests
def get_weather(city, api_key="c90a5414b5655205674b32ff578aad62"):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = { #query parameters
        'q': city, #city name
        'appid': api_key,#API key
        'units': 'metric'#to get temperature in Celsius
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return {
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description']
        }
    else:
        return None
if __name__ == "__main__":
    weather=get_weather("London")
    if weather:
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Description: {weather['description']}")
    else:
        print("City not found or API request failed.")