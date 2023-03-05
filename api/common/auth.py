from datetime import datetime, timedelta

from flask import request
import jwt

from common.config import config_auth
from common.exceptions import InvalidTokenError, ExpiredTokenError


def generate_token(account):
    payload = {
        'account': account,
        'exp': (
            datetime.utcnow() + timedelta(minutes=config_auth['expire_mins'])
        )
    }
    token = jwt.encode(
        payload, config_auth['secret_key'], algorithm=config_auth['token_algo']
    )
    return token


def jwt_required():
    token = request.headers.get('Authorization')
    token = token.split()[1] if token and len(token.split()) > 1 else None

    try:
        if token:
            jwt.decode(
                token, config_auth['secret_key'],
                algorithms=config_auth['token_algo']
            )
            return
        else:
            raise InvalidTokenError('權限錯誤')
    except jwt.ExpiredSignatureError:
        raise ExpiredTokenError('權限錯誤')
    except jwt.InvalidTokenError:
        raise InvalidTokenError('權限錯誤')
