from application.models.models import User
import pytest


# todo: Comment tests


def test_api_users(test_client):
    """
    API users should be able to list all users.
    API users should be able to create new user (register)
    API users should NOT be able to edit users on this endpoint
    """
    # Test Get users
    get_response = test_client.get('/api/users')
    users_response = get_response.json.get('users')
    users_in_db = User.query.all()
    assert get_response.status_code == 200
    assert type(users_response) is list
    assert len(users_in_db) == len(users_response)
    users_in_db_ids = [u.id for u in users_in_db]
    for user in users_response:
        assert user.get('id') in users_in_db_ids

    # Test Register User
    post_response = test_client.post('/api/users', json={'username': 'new_user', 'email': 'test@email.com'})
    assert post_response.status_code == 200
    assert post_response.json == {'success': 'User registered.'}
    user_in_db = User.query.filter_by(email='test@email.com').all()
    assert user_in_db is not None
    assert len(user_in_db) == 1
    user_in_db = user_in_db[0]
    assert user_in_db.username == 'new_user'
    assert user_in_db.verified is False
    assert len(user_in_db.responses) == 0
    assert len(user_in_db.adverts) == 0

    # Test Edit NOT allowed
    put_response = test_client.put('/api/users', json={'fake': 'data'})
    assert put_response.status_code == 405


def test_api_adverts(test_client):
    """
    API Users should only be able to list adverts.
    """
    pass
