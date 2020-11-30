import pytest
from tests import create_app


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app()
    testing_client = flask_app.test_client()
    ctx = flask_app.app_context()
    ctx.push()
    yield testing_client  # this is where the testing happens!
    ctx.pop()


# @pytest.fixture(scope='module')
# def db_init():
#     db.drop_all()
#     db.create_all()
#     LoadFakeData()

