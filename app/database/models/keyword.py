from sqlalchemy import String, BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.models.base import Base


class Keyword(Base):
    __tablename__ = 'keywords'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    word: Mapped[str]

    user: Mapped["User"] = relationship('User',
                        back_populates='words')
