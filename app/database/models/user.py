from sqlalchemy import String, BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.models.base import Base
from database.models.chat import Chat
from database.models.key import Key
from database.models.keyword import Keyword


class User(Base):
    __tablename__ = 'users'

    tg_id: Mapped[int] = mapped_column(BigInteger)
    is_admin: Mapped[bool] = mapped_column(default=False)

    key: Mapped[list['Key']] = relationship('Key', back_populates='user')
    words: Mapped[list["Keyword"]] = relationship('Keyword', back_populates='user')
    chats: Mapped[list["Chat"]] = relationship('Chat', back_populates='user')
