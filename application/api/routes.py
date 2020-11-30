from flask import (Blueprint, jsonify, current_app, request, url_for)
from application.models.models import (User, Advert)
from application.models.serializers import (userSerializer, advertSerializer, replySerializer)
import json


api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/')
def test():
    if current_app.config.get('ENV') == 'development':
        a = dict(current_app.config.items())
        a = dict(zip(a.keys(), map(str, a.values())))
        return jsonify(a)
    return {'prod': 1}


@api.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        username = request.json.get('username')
        email = request.json.get('email')
        exists = User.query.filter_by(email=email).first()
        if exists:
            return jsonify({'error': 'User already registered.'})
        User(username=username, email=email)
        return jsonify({'success': 'User registered.'})
    all_users = User.query.all()
    serialized_users = userSerializer.dumps(all_users, many=True)
    return jsonify(users=json.loads(serialized_users))


@api.route('/adverts', methods=['GET', 'POST'])
def adverts():
    if request.method == 'POST':

        return jsonify({'post': 1})

    all_adverts = sorted(Advert.query.all(), key=lambda ad: ad.timestamp, reverse=True)
    serialized_adverts = advertSerializer.dumps(all_adverts, many=True)
    return jsonify(adverts=json.loads(serialized_adverts), count=len(all_adverts))


@api.route('/adverts/<int:advert_id>')
def advert_detail(advert_id):
    advert = Advert.query.get(advert_id)
    if not advert:
        return jsonify(error='Nothing found.')
    serialized_advert = advertSerializer.dump(advert)
    return jsonify(serialized_advert)


@api.route('/adverts/<int:advert_id>/responses', methods=['GET', 'POST'])
def advert_detail_responses(advert_id):
    advert = Advert.query.get(advert_id)
    if not advert:
        return jsonify(error='Nothing found.')

    if request.method == 'POST':
        email = request.json.get('email')
        reply = request.json.get('reply')
        user = User.query.filter_by(email=email).first()
        if user:
            user.respond_to_advert(
                advert_id=advert.id,
                text=reply
            )
            return jsonify(success='Response sent.')
        return jsonify(error='Email is not registered.')
    sorted_responses = sorted(advert.responses, key=lambda resp: resp.timestamp, reverse=True)
    serialized_advert = replySerializer.dumps(sorted_responses, many=True)
    return jsonify(responses=json.loads(serialized_advert), advert_url=url_for('api.advert_detail', advert_id=advert.id, _external=True))


@api.route('/users/<int:user_id>')
def users_detail(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify(error='Nothing found.')
    serialized_user = userSerializer.dump(user)
    return jsonify(serialized_user)


@api.route('/users/<int:user_id>/adverts')
def user_adverts(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify(error='Nothing found.')
    serialized_user_adverts = advertSerializer.dumps(user.adverts, many=True)
    return jsonify(username=user.username,
                   count=len(user.adverts),
                   adverts=json.loads(serialized_user_adverts))


@api.route('/users/<int:user_id>/adverts/<int:advert_id>')
def user_advert_detail(user_id, advert_id):
    user = User.query.get(user_id)
    advert = Advert.query.get(advert_id)
    if not user or not advert:
        return jsonify(error='Nothing found.')
    if advert.user_id != user.id:
        return jsonify(warning='Permission denied.')
    serialized_advert = replySerializer.dump(advert)
    return jsonify(serialized_advert)


@api.route('/users/<user_id>/responses')
def user_responses(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify(error='Nothing found.')
    serialized_user_responses = replySerializer.dumps(user.responses, many=True)
    return jsonify(username=user.username,
                   count=len(user.responses),
                   responses=json.loads(serialized_user_responses))


@api.route('/users/<user_id>/adverts/<advert_id>/responses')
def users_advert_responses(user_id, advert_id):
    user = User.query.get(user_id)
    advert = Advert.query.get(advert_id)
    if advert.user_id != user.id:
        return jsonify(warning='Permission denied.')
    if not user or not advert:
        return jsonify(error='Nothing found.')
    serialized_responses = replySerializer.dumps(advert.responses, many=True)
    return jsonify(advert_id=advert.id, responses=json.loads(serialized_responses))
