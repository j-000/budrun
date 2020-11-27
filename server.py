from flask import Flask

from application.api.routes import api


def create_app():
    app = Flask(__name__)

    # Configure app
    if app.config.get('ENV') == 'production':
        app.config.from_object('config.ProdConfig')
    else:
        app.config.from_object('config.DevConfig')

    # Register Blueprints
    app.register_blueprint(api)
    return app
