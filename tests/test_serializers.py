import pytest
from application.models.serializers import (userSerializer, replySerializer, advertSerializer)


# test_client need to be passed to ensure app context is pushed.
@pytest.mark.usefixtures('test_client')
class TestSerializers:

    def test_userSerializer(self, random_user):
        field_types = {'user_url': str, 'username': str, 'id': int, 'responses': dict, 'adverts': dict, 'email': str,
                       'verified': bool, 'joined': str}
        allowed_fields_set = set(userSerializer.Meta.fields)
        ser_user = userSerializer.dump(random_user)
        ser_user_fields_set = set(ser_user.keys())
        # verify fields sent via serialized match to those in fields Meta class attribute
        assert ser_user_fields_set == allowed_fields_set
        # verify the type of each field is in field_types
        for field in ser_user_fields_set:
            assert type(ser_user.get(field)) is field_types.get(field)
        # verify the nested dictionaries are of the correct type and keys
        for (key, value) in filter(lambda v: v[1] is dict, field_types.items()):
            assert set(ser_user.get(key).keys()) == {'url', 'count'}
            assert set(map(type, ser_user.get(key).values())) == {str, int}

    def test_replySerializer(self, random_reply):
        field_types = {'id': int, 'timestamp': str, 'advert_id': int, 'text':str, 'user': str}
        allowed_fields_set = set(replySerializer.Meta.fields)
        ser_reply = replySerializer.dump(random_reply)
        ser_reply_fields_set = set(ser_reply.keys())
        # verify fields sent via serialized match to those in fields Meta class attribute
        assert ser_reply_fields_set == allowed_fields_set
        for field in ser_reply_fields_set:
            assert type(ser_reply.get(field)) is field_types.get(field)

    def test_advertSerializer(self, random_advert):
        field_types = {'id': int, 'title': str, 'timestamp': str, 'owner': str, 'text': str,
                       'location': str, 'responses': dict, 'advert_url': str}
        allowed_fields_set = set(advertSerializer.Meta.fields)
        ser_ad = advertSerializer.dump(random_advert)
        ser_ad_keys_set = set(ser_ad.keys())
        assert ser_ad_keys_set == allowed_fields_set
        for field in ser_ad_keys_set:
            assert type(ser_ad.get(field)) is field_types.get(field)
        for (key, value) in filter(lambda v: v[1] is dict, field_types.items()):
            assert set(ser_ad.get(key).keys()) == {'url', 'count'}
            assert set(map(type, ser_ad.get(key).values())) == {str, int}
