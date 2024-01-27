# This file is responsible for signing , encoding , decoding and returning JWTS
from datetime import datetime, timedelta
from typing import Annotated
from fastapi import Depends, HTTPException
from jwt import ExpiredSignatureError
from passlib.context import CryptContext
import jwt

from settings.auth_config import ALGORITHM, SECRET
from fastapi.security import OAuth2PasswordBearer

JWT_SECRET = SECRET
JWT_ALGORITHM = ALGORITHM

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='/api/v1/auth/login/')


def token_response(token: str):
    return {
        "access_token": token
    }


def create_access_token(data, expires_delta=timedelta(hours=3000)):
    encode = {'sub': data['email'], 'id': data['id']}
    expires = datetime.utcnow() + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET, algorithm=ALGORITHM)


def create_refresh_token(data):
    encode = {'sub': data['email'], 'id': data['id']}
    expires = datetime.utcnow() + timedelta(hours=3000)
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET, algorithm=ALGORITHM)


def decode_token(token, secret_key=SECRET, algorithm=ALGORITHM):
    payload = jwt.decode(token, secret_key, algorithms=[algorithm])
    return payload


async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        # decode token and extract username and expires data
        payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        email: str = payload.get('sub')
        id: int = payload.get('id')
        return {
            'email': email,
            'id': id,
        }
    except ExpiredSignatureError:
        return HTTPException(status_code=401, detail="Token has expired")
    except:
        raise HTTPException(status_code=401, detail="Something wrong with token")
