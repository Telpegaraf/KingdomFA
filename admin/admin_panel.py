from sqlalchemy import select
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from database import db_helper

from kingdom.models.user import User
from auth.utils import verify_password, hash_password


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        username = form.get("username")
        password = form.get("password")
        session = db_helper.get_scoped_session()
        query = select(User).where(User.username == username)
        result = await session.execute(query)
        user = result.scalars().first()
        if user and verify_password(plain_password=password, hashed_password=hash_password(password)):
            if user.is_superuser:
                request.session.update({"token": user.username})
                return True
        return False

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")
        return token is not None
