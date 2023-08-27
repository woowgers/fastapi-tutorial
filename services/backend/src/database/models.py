from datetime import datetime

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from src.database.config import BaseModel


class Base(BaseModel):
    __abstract__ = True

    created_dt: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    update_dt: Mapped[datetime] = mapped_column(
        default=datetime.utcnow, onupdate=datetime.utcnow
    )


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)
    full_name: Mapped[str] = mapped_column(String(128), nullable=False)
    password: Mapped[str] = mapped_column()

    def __str__(self):
        return f"User(username={self.username}, full_name={self.full_name})"

    def __repr__(self):
        return str(self)
