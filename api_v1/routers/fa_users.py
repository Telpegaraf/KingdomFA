from fastapi_users import FastAPIUsers
from api_v1.models.fastapi_users import TestUser
from api_v1.dependencies.authentication.user_manager import get_user_manager
from api_v1.dependencies.authentication.backend import authentication_backend
from api_v1.types.user_id import UserIdType


fastapi_users = FastAPIUsers[TestUser,UserIdType](
    get_user_manager,
    [authentication_backend]
)
