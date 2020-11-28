from wsgi import app
import random
# Workaround to start test db - Views functions will have access to current_app proxy, so no need to import.
from server import db
from application.models.models import User, Advert


def create_user():
    for i in range(1, 5):
        User(
            username=f'joao-{i}',
            email=f'jjasilva8{i}@gmail.com'
        )


def create_advert():
    for i in range(1, 10):
        joao = User.query.get(random.choice([1,2,3,4]))
        joao.create_advert(
            title='N15 Running Wednesday',
            text='Needs 3 people to join me for a run on Wednesday for a charity event. 2 PM.',
            location='N153ES'
        )


def create_response():
    for i in range(1, 4):
        joao = User.query.get(random.choice([1,2,3,4]))
        ad = Advert.query.get(random.choice([1,2,3,4]))
        joao.respond_to_advert(ad.id, f'Hi, {i} am interested!')


if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        create_user()
        create_advert()
        create_response()

