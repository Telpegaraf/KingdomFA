from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from api_v1.models.user import User
from core.config import settings
import database
from auth.utils import hash_password
import asyncio


async def create_superuser():
    user_name = settings.super_user.get("super_user_email")
    user_password = settings.super_user.get("super_user_password")
    user_password = hash_password(user_password)

    async with database.db_helper.session_factory() as session:
        async with session.begin():
            existing_user = await session.execute(
                select(User).where(User.username == user_name)
            )
            if existing_user.scalar_one_or_none():
                return

            superuser = User(
                username=user_name,
                password=user_password,
                email=user_name,
                is_superuser=True,
                is_active=True
            )
            session.add(superuser)
            await session.commit()
            await session.refresh(superuser)
            print(f"Superuser {superuser.username} created successfully.")


if __name__ == "__main__":
    asyncio.run(create_superuser())
