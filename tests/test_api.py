from application.models.models import User


# todo: Comment tests


def test_api_users(test_client):
    response = test_client.get('/api/users')
    users_response = response.json.get('users')
    users_in_db = User.query.all()
    assert response.status_code == 200
    assert type(users_response) is list
    assert len(users_in_db) == len(users_response)
    users_in_db_ids = [u.id for u in users_in_db]
    for user in users_response:
        assert user.get('id') in users_in_db_ids
