from datetime import datetime, timedelta
import settings
from jose import jwt, JWTError


def create_access_token(data: dict, expires_delta: timedelta = 0):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, settings.ALGORITHM)
    return encoded_jwt


def get_username_from_token(token: str):
    try:
        payload = decode_access_token(token)
        token_username: str = payload.get("sub")
        if not token_username:
            raise settings.CREDENTIAL_EXCEPTION
        return token_username
    except JWTError:
        raise settings.CREDENTIAL_EXCEPTION


def decode_access_token(data: str):
    return jwt.decode(data, settings.SECRET_KEY, settings.ALGORITHM)

