from starlette.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_current_date_times():
    params = {
        'city1': 'Chicago,IL',
        'city2': 'New York,NY'
    }
    response = client.get('/current_datetimes', params=params)
    assert response.status_code == 200
    assert len(response.json()['date']) == 2
    assert 'Chicago,IL' in response.json()['date']
    assert 'New York,NY' in response.json()['date']


def test_current_date_times_without_params():
    response = client.get('/current_datetimes')
    assert response.status_code == 422
