import os
import string
import random
from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, Request
from fastapi.openapi.models import OAuthFlows
from fastapi.security import OAuth2
from fastapi.security.utils import get_authorization_scheme_param
from jose import JWTError, jwt
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session
from src.database.config import get_db
from src.database.models import User
from src.schemas.token import Token

SECRET_KEY = os.environ.get("SECRET_KEY", ''.join(random.choices(string.ascii_letters, k=32)))
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class OAuth2PasswordBearerCookie(OAuth2):
    def __init__(
        self,
        token_url: str,
        maybe_scheme_name: str | None = None,
        maybe_scopes: dict | None = None,
        auto_error: bool = True,
    ):
        scheme_name = maybe_scheme_name or ""
        scopes = maybe_scopes or {}
        flows = OAuthFlows(password={"tokenUrl": token_url, "scopes": scopes})  # type: ignore
        super().__init__(flows=flows, scheme_name=scheme_name, auto_error=auto_error)

    def __call__(self, request: Request) -> str | None:
        authorization = request.cookies.get("Authorization")
        scheme, param = get_authorization_scheme_param(authorization)
        if not authorization or scheme.lower() != "bearer":
            if self.auto_error:
                raise HTTPException(
                    status_code=401,
                    detail="Not authenticated.",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            else:
                return None
        return param


security = OAuth2PasswordBearerCookie(token_url="/login")


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(token: str = Depends(security), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get('sub')
        if username is None:
            raise credentials_exception
        token_schema = Token(username=username)
    except JWTError:
        raise credentials_exception

    try:
        user = db.query(User).where(User.username == token_schema.username).one()
    except NoResultFound:
        raise credentials_exception

    return user
