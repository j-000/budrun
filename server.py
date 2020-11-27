from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from application.api.routes import api
from application.site.routes import site


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    # Configure app
    if app.config.get('ENV') == 'production':
        app.config.from_object('config.ProdConfig')
    else:
        app.config.from_object('config.DevConfig')

    # Update db handle with app config
    db.init_app(app)

    # Register Blueprints
    app.register_blueprint(api)
    app.register_blueprint(site)
    return app

