import unittest
from unittest.mock import patch
from favorites import add_to_favorites, remove_from_favorites, FAVORITE_CITIES
from weather_api import get_weather

class TestWeatherAPI(unittest.TestCase):
    @patch('weather_api.requests.get')
    def test_get_weather_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "cod": 200,
            "name": "Kyiv",
            "main": {"temp": 10, "humidity": 80},
            "weather": [{"description": "clear sky"}],
            "wind": {"speed": 5}
        }
        result = get_weather("Kyiv")
        self.assertIn("Місто: Kyiv", result)
        self.assertIn("Температура: 10°C", result)

    @patch('weather_api.requests.get')
    def test_get_weather_invalid_city(self, mock_get):
        mock_get.return_value.status_code = 404
        mock_get.return_value.json.return_value = {"cod": "404", "message": "city not found"}
        result = get_weather("InvalidCity")
        self.assertIn("Помилка: city not found", result)

    @patch('weather_api.requests.get', side_effect=Exception("HTTP Error"))
    def test_get_weather_http_error(self, mock_get):
        result = get_weather("Kyiv")
        self.assertIn("Помилка HTTP: HTTP Error", result)


class TestFavorites(unittest.TestCase):
    def setUp(self):
        FAVORITE_CITIES.clear()

    def test_add_to_favorites_success(self):
        favorites_list_mock = unittest.mock.MagicMock()
        add_to_favorites("Kyiv", favorites_list_mock)
        self.assertIn("Kyiv", FAVORITE_CITIES)
        favorites_list_mock.insert.assert_called_with(0, "Kyiv")

    def test_add_to_favorites_duplicate(self):
        favorites_list_mock = unittest.mock.MagicMock()
        add_to_favorites("Kyiv", favorites_list_mock)
        add_to_favorites("Kyiv", favorites_list_mock)
        self.assertEqual(FAVORITE_CITIES.count("Kyiv"), 1)

    def test_remove_from_favorites_success(self):
        FAVORITE_CITIES.append("Kyiv")
        favorites_list_mock = unittest.mock.MagicMock()
        favorites_list_mock.get.return_value = "Kyiv"
        remove_from_favorites(favorites_list_mock)
        self.assertNotIn("Kyiv", FAVORITE_CITIES)

    def test_remove_from_favorites_no_selection(self):
        favorites_list_mock = unittest.mock.MagicMock()
        favorites_list_mock.get.side_effect = IndexError
        with self.assertRaises(IndexError):
            remove_from_favorites(favorites_list_mock)


if __name__ == "__main__":
    unittest.main()
