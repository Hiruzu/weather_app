import pytest
import requests
from unittest.mock import patch
from app.backend import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

@patch("requests.get")
def test_weather(mock_get, client):
    mock_response = {
        "city": "Paris",
        "temperature": 15,
        "description": "ciel dégagé",
    }

    mock_get.return_value.json.return_value = mock_response
    mock_get.return_value.status_code = 200

    response = client.get("/weather?city=Paris")
    
    assert response.status_code == 200
    assert response.json == mock_response

@patch("requests.get")
def test_air_quality(mock_get, client):
    mock_response = {
        "city": "Paris",
        "aqi": 2,
        "description": "Air modérément pollué",
    }

    mock_get.return_value.json.return_value = mock_response
    mock_get.return_value.status_code = 200

    response = client.get("/air_quality?city=Paris")
    
    assert response.status_code == 200
    assert response.json == mock_response

@patch("requests.get")
def test_uv_index(mock_get, client):
    mock_response = {
        "city": "Paris",
        "uv_index": 5,
        "description": "Modéré",
    }

    mock_get.return_value.json.return_value = mock_response
    mock_get.return_value.status_code = 200

    response = client.get("/uv_index?city=Paris")
    
    assert response.status_code == 200
    assert response.json == mock_response

