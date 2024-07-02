from fastapi_users import FastAPIUsers
from api_v1.models.user_test import TestUser
from api_v1.dependencies.user_manager import get_user_manager
from api_v1.dependencies.backend import authentication_backend
from api_v1.types.user_id import UserIdType


fastapi_users = FastAPIUsers[TestUser,UserIdType](
    get_user_manager,
    [authentication_backend]
)
