from fastapi import status, Depends, APIRouter
from fastapi.security import HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from kingdom.crud import god as crud
from kingdom.schemas import god as schemas
from kingdom.models import religion as models
from kingdom.dependencies.get_object import get_object_by_id_dependency
from auth.utils import get_current_token_payload
from database import db_helper

http_bearer = HTTPBearer(auto_error=False)

god_router = APIRouter(prefix="/god", tags=["Gods"], dependencies=[Depends(http_bearer)])



