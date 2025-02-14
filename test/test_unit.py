import unittest
import json
from unittest.mock import patch
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))
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

        response_json = json.loads(response.data)
        self.assertEqual(response_json["description"], "ciel dégagé")
        self.assertEqual(response_json["temperature"], 20)

    @patch("backend.requests.get")
    def test_weather_invalid_city(self, mock_get):
        mock_get.return_value.json.return_value = {"cod": "404", "message": "city not found"}

        response = self.client.get("/weather?city=FakeCity")
        self.assertEqual(response.status_code, 404)

        response_json = json.loads(response.data)
        self.assertEqual(response_json["error"].lower(), "ville non trouvée.".lower())

    @patch("backend.requests.get")
    def test_air_quality_valid_city(self, mock_get):
        mock_get.return_value.json.return_value = {
            "coord": {"lat": 48.8566, "lon": 2.3522},
            "list": [{"main": {"aqi": 3}}]
        }

        response = self.client.get("/air_quality?city=Paris")
        self.assertEqual(response.status_code, 200)
        
        response_json = json.loads(response.data)
        self.assertIn("air_quality_index", response_json)

    @patch("backend.requests.get")
    def test_uv_index_valid_city(self, mock_get):
    
        mock_get.side_effect = [
            unittest.mock.Mock(json=lambda: {"coord": {"lat": 48.8566, "lon": 2.3522}}, status_code=200),
        
            unittest.mock.Mock(json=lambda: {"value": 1.3}, status_code=200)  #
        ]

        response = self.client.get("/uv_index?city=Paris")

        print("DEBUG Response:", response.status_code, response.data) 

        self.assertEqual(response.status_code, 200)

        response_json = json.loads(response.data)
        self.assertEqual(response_json["uv_index"], 1.3)  

if __name__ == "__main__":
    unittest.main()

