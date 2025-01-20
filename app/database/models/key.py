from sqlalchemy import String, BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.models.base import Base
from database.tools import _generate_cuid


class Key(Base):
    __tablename__ = 'keys'

    value: Mapped[str] = mapped_column(default=_generate_cuid)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=True)

    user: Mapped["User"] = relationship('User', back_populates='key')

