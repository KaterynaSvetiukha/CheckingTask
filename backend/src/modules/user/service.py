from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from pwdlib import PasswordHash

from .mapper import user_to_response
from .models import UserModel
from .schemas import Register, Login

password_hash = PasswordHash.recommended()

async def get_user_by_id(session: AsyncSession, user_id: str):
    user = await session.get(UserModel, user_id)

    if not user:
        return None
    
    return user_to_response(user)

async def create(session: AsyncSession, user: Register) -> UserModel | None:
    user_data = user.model_dump()
    user_data["password"] = password_hash.hash(user.password)

    username_result = await session.execute(
        select(UserModel.id).where(UserModel.username == user.username)
    )

    if username_result.scalar_one_or_none() is not None:
        return None

    email_result = await session.execute(
        select(UserModel.id).where(UserModel.email == user.email)
    )

    if email_result.scalar_one_or_none() is not None:
        return None

    new_user = UserModel(**user_data)

    session.add(new_user)
    try:
        await session.commit()
    except IntegrityError:
        await session.rollback()
        return None

    await session.refresh(new_user)

    return new_user

async def login_user(session: AsyncSession, user: Login) -> UserModel | None:
    result = await session.execute(
        select(UserModel).where(UserModel.email == user.email)
    )
    stored_user = result.scalar_one_or_none()

    if not stored_user or not password_hash.verify(user.password, stored_user.password):
        return None

    return stored_user

async def delete(session: AsyncSession, user_id: str):
    user = await session.get(UserModel, user_id)

    if not user:
        return None

    await session.delete(user)
    await session.commit()
    return True