from fastapi import HTTPException
from passlib.context import CryptContext
from sqlalchemy.exc import IntegrityError, NoResultFound
from sqlalchemy.orm import Session
from src.database.models import User
from src.schemas.token import Status
from src.schemas.users import UserCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def read_all_users(db: Session) -> list[User]:
    return db.query(User).all()


def read_user(id: int, db: Session) -> User:
    return db.query(User).where(User.id == id).one()


def create_user(schema: UserCreate, db: Session) -> User:
    schema.password = pwd_context.encrypt(schema.password)
    try:
        user = User(**schema.model_dump())
        db.add(user)
        db.commit()
    except IntegrityError:
        raise HTTPException(status_code=401, detail="Failed to create user.")
    return user


def delete_user(id: int, current_user: User, db: Session) -> Status:
    try:
        user = db.query(User).where(User.id == id).one()
    except NoResultFound:
        raise HTTPException(status_code=404, detail="User not found.")

    if user.id != current_user.id:
        raise HTTPException(
            status_code=403, detail="Not authorized to delete this user."
        )

    deleted_count = db.query(User).filter(User.id == id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail="User not found.")

    db.commit()
    return Status(message="User has been deleted.")
