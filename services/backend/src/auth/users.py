from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from src.database.models import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(password: str, pwhash: str) -> bool:
    return pwd_context.verify(password, pwhash)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def get_user(username: str, db: Session) -> User:
    return db.query(User).where(User.username == username).one()


def validate_user(db: Session, user_form: OAuth2PasswordRequestForm = Depends()):
    def make_unauthorized_error():
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials.")

    try:
        user = get_user(user_form.username, db)
    except NoResultFound:
        raise make_unauthorized_error()

    if not verify_password(user_form.password, user.password):
        raise make_unauthorized_error()

    return user
