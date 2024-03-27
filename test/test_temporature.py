from starlette.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_temperature():
    params = {
        'city1': 'Chicago,IL',
        'city2': 'New York,NY'
    }
    response = client.get('/current_datetimes_temp', params=params)
    assert response.status_code == 200
    assert len(response.json()['info']) == 2
    assert 'Chicago,IL' in response.json()['info']
    assert 'New York,NY' in response.json()['info']


def test_temperature_without_params():
    response = client.get('/current_datetimes_temp')
    assert response.status_code == 422
