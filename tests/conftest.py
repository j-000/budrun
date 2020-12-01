import pytest
from tests import create_app
from application.models.models import (User, Reply, Advert)
import random


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app()
    testing_client = flask_app.test_client()
    ctx = flask_app.app_context()
    ctx.push()
    yield testing_client  # this is where the testing happens!
    ctx.pop()


@pytest.fixture(scope='function')
def random_user():
    r_user = random.choice(User.query.all())
    return r_user


@pytest.fixture(scope='function')
def random_reply():
    r_reply = random.choice(Reply.query.all())
    return r_reply


@pytest.fixture(scope='function')
def random_advert():
    r_advert = random.choice(Advert.query.all())
    return r_advert
