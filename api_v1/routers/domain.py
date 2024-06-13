from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.dependencies.domain import get_domain_by_id
from api_v1.crud import domain as crud
from api_v1.schemas import domain as schemas
from api_v1.models import domain as models
from database import db_helper


domain_router = APIRouter(prefix="/domain", tags=["Domains"])


@domain_router.post("/create/", response_model=schemas.DomainBase, status_code=status.HTTP_201_CREATED)
async def domain_create(
        domain_in: schemas.DomainBase,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    result = await crud.domain_create(domain_in=domain_in, session=session)
    return result


@domain_router.get("/{domain_id}/")
async def domain_detail(
        domain: models.Domain = Depends(get_domain_by_id)
):
    return domain


@domain_router.get("/", response_model=list[schemas.Domain])
async def domain_list(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    result = await crud.domain_list(session=session)
    return result


@domain_router.patch("/update/{domain_id}/")
async def domain_update(
        domain_update: schemas.DomainUpdate,
        domain: models.Domain = Depends(get_domain_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.domain_update(
        domain_update=domain_update,
        domain=domain,
        session=session,
    )


@domain_router.delete("/delete/{domain_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def domain_delete(
        domain: models.Domain = Depends(get_domain_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    await crud.domain_delete(domain=domain, session=session)
