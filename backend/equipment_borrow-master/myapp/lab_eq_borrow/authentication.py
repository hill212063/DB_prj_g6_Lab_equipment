import jwt, datetime
from rest_framework import exceptions

def create_access_token(id,role):
 
    return jwt.encode({
        'user_id': id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
        'iat': datetime.datetime.utcnow(),
        'user_role' : role
    }, 'access_secret', algorithm='HS256')

def decode_access_token(token):
    try:
        payload = jwt.decode(token, 'access_secret', algorithms='HS256')

        return payload['user_id'], payload['user_role']
    except:
        raise exceptions.AuthenticationFailed('unauthenticated')

def create_refresh_token(id,role):
    return jwt.encode({
        'user_id': id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
        'iat': datetime.datetime.utcnow(),
        'user_role' : role
    }, 'refresh_secret', algorithm='HS256')

def decode_refresh_token(token):
    try:
        payload = jwt.decode(token, 'refresh_secret', algorithms='HS256')
        print(payload)
        return payload['user_id'], payload['user_role']
    except:
        raise exceptions.AuthenticationFailed('unauthenticated')