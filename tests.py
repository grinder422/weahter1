import unittest
from favorites import add_to_favorites, remove_from_favorites, FAVORITE_CITIES
from weather_api import get_weather


class TestWeatherAppIntegration(unittest.TestCase):
    def setUp(self):
        # Очищення списку улюблених перед кожним тестом
        FAVORITE_CITIES.clear()

    def test_get_weather_success(self):
        city = "Kyiv"
        result = get_weather(city)
        self.assertIn("Місто: Kyiv", result)

    def test_add_to_favorites(self):
        city = "Lviv"
        add_to_favorites(city, None)
        self.assertIn(city, FAVORITE_CITIES)

    def test_remove_from_favorites(self):
        city = "Sumy"
        add_to_favorites(city, None)
        self.assertIn(city, FAVORITE_CITIES)

        # Видалення
        FAVORITE_CITIES.remove(city)
        self.assertNotIn(city, FAVORITE_CITIES)

    def test_add_duplicate_to_favorites(self):
        city = "Kharkiv"
        add_to_favorites(city, None)
        add_to_favorites(city, None)  # Спроба додати вдруге
        self.assertEqual(FAVORITE_CITIES.count(city), 1)


if __name__ == "__main__":
    unittest.main()


