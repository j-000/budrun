from wsgi import app
# Workaround to start test db - Views functions will have access to current_app proxy, so no need to import.
from server import db

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
