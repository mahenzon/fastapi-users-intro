from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy import (
    SQLAlchemyBaseUserTable,
    SQLAlchemyUserDatabase,
)
from sqlalchemy.orm import relationship, Mapped

from core.types.user_id import UserIdType
from .base import Base
from .mixins.id_int_pk import IdIntPkMixin

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession
    from core.models import AccessToken


class User(Base, IdIntPkMixin, SQLAlchemyBaseUserTable[UserIdType]):
    access_tokens: Mapped[list["AccessToken"]] = relationship(
        back_populates="user",
    )

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, cls)

    def __str__(self):
        return self.email
