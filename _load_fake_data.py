import random
import time
from server import *
from application.models.models import *

app.config.from_object('config.DevConfig')
app.app_context().push()


users = [
    {
        'username': 'Ana',
        'email': 'ana@live.com'
    },
    {
        'username': 'Joao',
        'email': 'joao@live.com'
    },
    {
        'username': 'Goncalo',
        'email': 'goncalo@live.com'
    },
    {
        'username': 'Rodrigo',
        'email': 'rodrigo@live.com'
    }
]
adverts = [
    {
        'title': 'Fun RUN',
        'text': '10 Secret Things You Didn\'t Know About RUN',
        'location': 'N15'
    },
    {
        'title': 'The Best Way To RUN',
        'text': '10 Secret Things You Didn\'t Know About RUN',
        'location': 'N16'
    },
    {
        'title': 'Hot RUN',
        'text': '12 Secret Things Didn\'t Know About RUN',
        'location': 'N1S7'
    },
    {
        'title': 'Bat RUN',
        'text': '10 Things You Didn\'t Know About RUN',
        'location': 'SN15'
    },
    {
        'title': 'Cat To RUN',
        'text': '10 Secret Things You Didn\'t Know About RUN',
        'location': 'N16'
    },
    {
        'title': 'Hot RUN',
        'text': '192 Secret Things You Didn\'t Know About RUN',
        'location': 'QN17'
    },
    {
        'title': 'Dog RUN',
        'text': '1wd0 Things You Didn\'t Know About RUN',
        'location': 'SsN125'
    },
    {
        'title': 'Rabbit To RUN',
        'text': '1wdw0 Secret Things You Didn\'t Know About RUN',
        'location': 'N106'
    },
    {
        'title': 'Beaver RUN',
        'text': '1dd92 Secret Things You Didn\'t Know About RUN',
        'location': 'WN17'
    }]
responses = [
    {
        'advert_id': '',
        'text':''
    }
]


class LoadFakeData:
    def __init__(self):
        db.drop_all()
        db.create_all()
        self._load_users()
        self._load_adverts()
        self._load_responses()

    def _load_users(self):
        for user in users:
            User(username=user.get('username'), email=user.get('email'))

    def _load_adverts(self):
        db_users = User.query.all()
        for _ in range(10):
            u = random.choice(db_users)
            ad = random.choice(adverts)
            u.create_advert(
                title=ad.get('title'),
                text=ad.get('text'),
                location=ad.get('location')
            )
            time.sleep(1)

    def _load_responses(self):
        for _ in range(15):
            u = random.choice(User.query.all())
            ad = random.choice(Advert.query.all())
            if ad.user.id != u.id:  # owners should not reply to themselves
                u.respond_to_advert(
                    advert_id=ad.id,
                    text=f'{u.username} is interested!'
                )
                time.sleep(1)


if __name__ == '__main__':
    LoadFakeData()
