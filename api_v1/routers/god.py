from fastapi import status, Depends, APIRouter
from fastapi.security import HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.crud import god as crud
from api_v1.schemas import god as schemas
from api_v1.models import religion as models
from api_v1.dependencies.get_object import get_object_by_id_dependency
from auth.utils import get_current_token_payload
from database import db_helper

http_bearer = HTTPBearer(auto_error=False)

god_router = APIRouter(prefix="/god", tags=["Gods"], dependencies=[Depends(http_bearer)])



