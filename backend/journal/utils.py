import json

import jwt  
import requests
from django.contrib.auth import authenticate
from django.conf import settings
from jose import jwt as jose_jwt

def jwt_decode_token(token):
    header = jwt.get_unverified_header(token)
    jwks = requests.get('https://{}/.well-known/jwks.json'.format(settings.SOCIAL_AUTH_AUTH0_DOMAIN)).json()
    public_key = None

    for jwk in jwks['keys']:
        if jwk['kid'] == header['kid']:
            public_key = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(jwk))

    if public_key is None:
        raise Exception('Public key not found.')

    issuer = 'https://{}/'.format(settings.SOCIAL_AUTH_AUTH0_DOMAIN)
    return jwt.decode(token, public_key, audience=settings.SOCIAL_AUTH_AUTH0_KEY, issuer=issuer, algorithms=['RS256'])


def jwt_get_username_from_payload_handler(payload):
    username = payload.get('sub').replace('|', '.')
    authenticate(remote_user=username)
    return username
