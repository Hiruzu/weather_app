import unittest
import sys
sys.path.append(".")
from unittest.mock import patch
import backend

class WeatherAPITest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """ Démarre une instance Flask pour les tests """
        backend.app.testing = True
        cls.client = backend.app.test_client()

    @patch("backend.requests.get")
    def test_home(self, mock_get):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Welcome to the Weather API".encode("utf-8"), response.data)

    @patch("backend.requests.get")
    def test_weather_valid_city(self, mock_get):
        mock_get.return_value.json.return_value = {
            "main": {"temp": 20},
            "weather": [{"description": "ciel dégagé"}]
        }

        response = self.client.get("/weather?city=Paris")
        self.assertEqual(response.status_code, 200)
        self.assertIn("temperature".encode("utf-8"), response.data)
        self.assertIn("ciel dégagé".encode("utf-8"), response.data)

    @patch("backend.requests.get")
    def test_weather_invalid_city(self, mock_get):
        mock_get.return_value.json.return_value = {"cod": "404", "message": "city not found"}

        response = self.client.get("/weather?city=FakeCity")
        self.assertEqual(response.status_code, 404)
        self.assertIn("Ville non trouvee".encode("utf-8"), response.data.lower())  # Correction

    @patch("backend.requests.get")
    def test_air_quality_valid_city(self, mock_get):
        mock_get.return_value.json.return_value = {
            "coord": {"lat": 48.8566, "lon": 2.3522},
            "list": [{"main": {"aqi": 3}}]
        }

        response = self.client.get("/air_quality?city=Paris")
        self.assertEqual(response.status_code, 200)
        self.assertIn("air_quality_index".encode("utf-8"), response.data)

    @patch("backend.requests.get")
    def test_uv_index_valid_city(self, mock_get):
        mock_get.return_value.json.return_value = {"value": 5.5}

        response = self.client.get("/uv_index?city=Paris")
        self.assertEqual(response.status_code, 200)
        self.assertIn("uv_index".encode("utf-8"), response.data)

if __name__ == "__main__":
    unittest.main()

