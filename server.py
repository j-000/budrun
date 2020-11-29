from flask import (Flask, render_template)
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

from application.api.routes import api


def create_app():
    app = Flask(__name__,
                template_folder='./frontend/dist',
                static_folder='./frontend/dist/static',
                )  # Todo: Find a way to load this via config.Config
    # Config app based on FLAKS_ENV var
    if app.config.get('ENV') == 'production':
        app.config.from_object('config.ProdConfig')
    else:
        app.config.from_object('config.DevConfig')
    # Update db handle with app config
    db.init_app(app)
    # Update ma handle with app config
    ma.init_app(app)
    # Register Blueprints
    app.register_blueprint(api)
    return app


app = create_app()
CORS(app=app, resources={r'/*': {'origins': '*'}})  # Todo: change this dynamically based on ENV


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')


