import requests

API_KEY = '6e2ebf08cb24f66749f31d738195849b'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    try:
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric&lang=ua"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data["cod"] == 200:
            weather = f"""
Місто: {data['name']}
Температура: {data['main']['temp']}°C
Вологість: {data['main']['humidity']}%
Опис: {data['weather'][0]['description']}
Вітер: {data['wind']['speed']} м/с
"""
            return weather
        else:
            return f"Помилка: {data.get('message', 'Невідома помилка')}"
    except requests.exceptions.RequestException as e:
        return f"Помилка HTTP: {e}"
    except Exception as e:
        return f"Інша помилка: {e}"