from fastapi_users import FastAPIUsers
from kingdom.models.fastapi_users import TestUser
from kingdom.dependencies.authentication.user_manager import get_user_manager
from kingdom.dependencies.authentication.backend import authentication_backend
from kingdom.types.user_id import UserIdType


fastapi_users = FastAPIUsers[TestUser,UserIdType](
    get_user_manager,
    [authentication_backend]
)
