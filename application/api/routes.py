from flask import (Blueprint, jsonify)

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/')
def test():
    return jsonify({'test': 'api'})
