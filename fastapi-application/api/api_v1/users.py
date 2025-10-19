from typing import TYPE_CHECKING, Annotated

from fastapi import APIRouter, Depends

from api.dependencies.authentication import get_users_db
from core.authentication.fastapi_users import fastapi_users
from core.config import settings
from core.schemas.user import (
    UserRead,
    UserUpdate,
)

if TYPE_CHECKING:
    from core.models import User
    from core.models.user import SQLAlchemyUserDatabase

router = APIRouter(
    prefix=settings.api.v1.users,
    tags=["Users"],
)


@router.get(
    "",
    response_model=list[UserRead],
)
# async def get_users_list() -> list[UserRead]:
async def get_users_list(
    users_db: Annotated[
        "SQLAlchemyUserDatabase",
        Depends(get_users_db),
    ],
) -> list["User"]:
    return await users_db.get_users()


# /me
# /{id}
router.include_router(
    router=fastapi_users.get_users_router(
        UserRead,
        UserUpdate,
    ),
)
