from flask import (Blueprint, jsonify, current_app)


api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/')
def test():
    if current_app.config.get('ENV') == 'development':
        a = dict(current_app.config.items())
        a = dict(zip(a.keys(), map(str, a.values())))
        return jsonify(a)
    return jsonify({'test': ''})