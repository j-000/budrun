from server import db
import datetime


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    joined = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    username = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    verified = db.Column(db.Boolean, default=False)
    adverts = db.relationship('Advert', backref='user', lazy=True)
    responses = db.relationship('Reply', backref='user', lazy=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'<User:{self.id}:{self.username}>'

    def create_advert(self, title, text, location):
        Advert(
            user_id=self.id,
            title=title,
            text=text,
            location=location
        )

    def respond_to_advert(self, advert_id, text):
        advert = Advert.query.get(advert_id)
        advert.respond_to_advert(text, self.id)


class Advert(db.Model):
    __tablename__ = 'adverts'

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(50), nullable=False)
    text = db.Column(db.Text(), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    responses = db.relationship('Reply', backref='advert', lazy=True)

    def __init__(self, user_id, title, text, location):
        self.user_id = user_id
        self.title = title
        self.text = text
        self.location = location
        db.session.add(self)
        db.session.commit()

    def respond_to_advert(self, text, user_id):
        message = Reply(
            text=text,
            user_id=user_id
        )
        self.responses.append(message)
        db.session.add(self)
        db.session.commit()

    def get_formatted_timestamp(self):
        return self.timestamp.strftime("%d/%m/%Y at %H:%M:%S")


class Reply(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    advert_id = db.Column(db.Integer, db.ForeignKey('adverts.id'))
    text = db.Column(db.Text(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, text, user_id):
        self.text = text
        self.user_id = user_id
        db.session.add(self)
        db.session.commit()
