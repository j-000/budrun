from flask import url_for
from server import ma
from application.models.models import User, Reply, Advert


class UserSerializer(ma.SQLAlchemySchema):
    class Meta:
        model = User
        fields = ['id', 'username', 'joined', 'email',
                  'verified', 'adverts', 'user_url', 'responses']
    joined = ma.Function(lambda user: user.joined.strftime("%d/%m/%Y at %H:%M:%S"))

    adverts = ma.Function(lambda user: {
        'count': len(user.adverts),
        'url': url_for('api.user_adverts', user_id=user.id, _external=True)
    })
    responses = ma.Function(lambda user: {
        'count': len(user.responses),
        'url': url_for('api.user_responses', user_id=user.id, _external=True)
    })
    user_url = ma.Function(lambda user: url_for('api.users_detail', user_id=user.id, _external=True))


class AdvertSerializer(ma.SQLAlchemySchema):
    class Meta:
        model = Advert
        fields = ['id', 'title', 'timestamp', 'user_id', 'text',
                  'location', 'responses', 'url']
    responses = ma.Function(lambda advert: {
        'count': len(advert.responses),
        'url': url_for('api.users_advert_responses', user_id=advert.user_id, advert_id=advert.id, _external=True)
    })
    url = ma.Function(lambda advert: url_for('site.advert_detail', advert_id=advert.id, _external=True))


class ReplySerializer(ma.SQLAlchemySchema):
    class Meta:
        model = Reply
        fields = ['id', 'timestamp', 'advert_id', 'text', 'user_id']






userSerializer = UserSerializer()
replySerializer = ReplySerializer()
advertSerializer = AdvertSerializer()
