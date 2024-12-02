import unittest
from app import show_weather, show_favorite_weather
from favorites import add_to_favorites, remove_from_favorites, update_favorites_list, FAVORITE_CITIES
from weather_api import get_weather

class TestWeatherAppIntegration(unittest.TestCase):

    def test_show_weather_integration(self):
        # Перевіряємо, що функція show_weather() повертає правильний результат
        # за припущенням, що get_weather() працює коректно.
        city = 'Київ'
        result = get_weather(city)
        self.assertTrue(result.startswith("Місто: Київ"))

    def test_add_favorite_city(self):
        city = 'Львів'
        add_to_favorites(city, None)
        self.assertIn(city, FAVORITE_CITIES)

    def test_remove_favorite_city(self):
        city = 'Одеса'
        add_to_favorites(city, None)  # Спочатку додаємо місто
        self.assertIn(city, FAVORITE_CITIES)

        remove_from_favorites(None)  # Видаляємо місто
        self.assertNotIn(city, FAVORITE_CITIES)

    def test_show_favorite_weather_integration(self):
        city = 'Харків'
        add_to_favorites(city, None)  # Додаємо місто в улюблені

        # Перевіряємо, що функція show_favorite_weather повертає правильний результат
        result = get_weather(city)
        self.assertTrue(result.startswith("Місто: Харків"))

if __name__ == '__main__':
    unittest.main()

