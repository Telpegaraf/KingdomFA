from fastapi_users.authentication import (
    AuthenticationBackend,
)

from api_v1.authentication.transport import bearer_transport
from api_v1.dependencies.authentication.strategy import get_database_strategy


authentication_backend = AuthenticationBackend(
    name='access-tokens-db',
    transport=bearer_transport,
    get_strategy=get_database_strategy
)