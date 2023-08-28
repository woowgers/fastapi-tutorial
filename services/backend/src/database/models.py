from datetime import datetime

from sqlalchemy import Column, String, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm.properties import ForeignKey

from src.database.config import BaseModel

Friendship = Table(
    "friendship",
    BaseModel.metadata,
    Column("left_id", ForeignKey("user.id"), primary_key=True),
    Column("right_id", ForeignKey("user.id"), primary_key=True),
)


class Base(BaseModel):
    __abstract__ = True

    create_dt: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    update_dt: Mapped[datetime] = mapped_column(default=datetime.utcnow, onupdate=datetime.utcnow)


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)
    full_name: Mapped[str] = mapped_column(String(128), nullable=False)
    password: Mapped[str] = mapped_column()

    friends: Mapped[list['User']] = relationship(
        secondary=Friendship,
        primaryjoin=Friendship.c.left_id == id,
        secondaryjoin=Friendship.c.right_id == id,
        cascade='delete',
    )

    def __str__(self):
        return f"User(username={self.username}, full_name={self.full_name})"

    def __repr__(self):
        return str(self)
