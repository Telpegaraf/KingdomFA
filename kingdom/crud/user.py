import logging

import sqlalchemy.exc
from fastapi import HTTPException, status, Depends
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from asyncpg.exceptions import UniqueViolationError

from kingdom.models.user import User
from kingdom.schemas.user import (
    UserBase,
    UserUpdatePassword,
    UserValidate
)
from auth.utils import hash_password, verify_password
import database


async def user_detail(session: AsyncSession, user_id: int) -> User | None:
    return await session.get(User, user_id)


async def user_list(session: AsyncSession) -> list[User]:
    stmt = select(User).order_by(User.id)
    result: Result = await session.execute(stmt)
    users = result.scalars().all()
    return list(users)


async def user_create(
        session: AsyncSession,
        user_in: UserBase,
) -> User:
    user_password = hash_password(user_in.password)
    user = User(
        username=user_in.username,
        password=user_password,
        email=user_in.email,
    )
    session.add(user)
    try:
        await session.commit()
        await session.refresh(user)
    except sqlalchemy.exc.IntegrityError as e:
        if "users_username_key" in str(e.orig):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="This username already exists"
            )
        elif "users_email_key" in str(e.orig):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="This email already exists"
            )
    return user


async def change_password(
        session: AsyncSession,
        user: User,
        user_in: UserUpdatePassword
) -> User:
    if verify_password(user_in.old_password, user.password):
        user.password = hash_password(user_in.new_password)
        await session.commit()
        await session.refresh(user)
        return user
    else:
        raise ValueError("Old password does not match")


async def validate_user(
        user_in: UserValidate,
        session: AsyncSession = Depends(database.db_helper.scoped_session_dependency)
):
    stmt = select(User).where(User.username == user_in.username)
    result = await session.execute(stmt)
    user = result.scalars().first()
    if not user or not verify_password(user_in.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    return user


async def user_delete(
        user: User,
        session: AsyncSession
):
    await session.delete(user)
    await session.commit()
