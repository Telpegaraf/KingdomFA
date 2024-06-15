from fastapi import APIRouter, status, Depends
from fastapi.security import HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.dependencies import get_object_by_id_dependency
from api_v1.crud import domain as crud
from api_v1.schemas import domain as schemas
from api_v1.models import domain as models
from database import db_helper
from auth.utils import get_current_token_payload

http_bearer = HTTPBearer(auto_error=False)

#domain_router = APIRouter(prefix="/domain", tags=["Domains"])
domain_router = APIRouter(prefix="/domain", tags=["Domains"], dependencies=[Depends(http_bearer)])


@domain_router.get("/{object_id}/")
async def domain_detail(
    payload: dict = Depends(get_current_token_payload),
    domain: models.Domain = Depends(get_object_by_id_dependency(models.Domain))
):
    return domain


@domain_router.get("/", response_model=list[schemas.Domain])
async def domain_list(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    result = await crud.domain_list(session=session)
    return result


@domain_router.post("/create/", response_model=schemas.DomainBase, status_code=status.HTTP_201_CREATED)
async def domain_create(
        domain_in: schemas.DomainBase,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    result = await crud.domain_create(domain_in=domain_in, session=session)
    return result


@domain_router.patch("/update/{object_id}/")
async def domain_update(
        domain_update: schemas.DomainUpdate,
        domain: models.Domain = Depends(get_object_by_id_dependency(models.Domain)),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.domain_update(
        domain_update=domain_update,
        domain=domain,
        session=session,
    )


@domain_router.delete("/delete/{object_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def domain_delete(
        domain: models.Domain = Depends(get_object_by_id_dependency(models.Domain)),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    await crud.domain_delete(domain=domain, session=session)
