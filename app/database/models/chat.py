from sqlalchemy import String, BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.models.base import Base


class Chat(Base):
    __tablename__ = 'chats'

    tg_id: Mapped[int] = mapped_column(BigInteger)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    link: Mapped[str]
    name: Mapped[str]

    user: Mapped["User"] = relationship('User', back_populates='chats')