import requests


ROOT_URL = 'http://127.0.0.1:5000/api'


def test_api_test_route():
    response = requests.get(f'{ROOT_URL}/')
    assert response.status_code == 200
