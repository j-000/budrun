

def test_home_view(test_client):
    response = test_client.get('/')
    assert response.status_code == 200

