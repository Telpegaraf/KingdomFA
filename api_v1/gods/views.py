from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.gods import models, schemas, crud, dependencies
from database import db_helper


gods_router = APIRouter(prefix="/gods")


@gods_router.get("/domain/{domain_id}/")
async def domain_detail(
        domain: models.Domain = Depends(dependencies.get_domain_by_id)
):
    return domain


@gods_router.post("/domain/", response_model=schemas.DomainBase, status_code=status.HTTP_201_CREATED)
async def create_domain(
        domain_in: schemas.DomainBase,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    result = await crud.domain_create(domain_in=domain_in,session=session)
    return result


@gods_router.get("/domain_list/", response_model=list[schemas.Domain])
async def domain_list(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    result = await crud.domain_list(session=session)
    return result


@gods_router.patch("/domain_update/{domain_id}/")
async def domain_update(
        domain_update: schemas.DomainBase,
        domain: models.Domain = Depends(dependencies.get_domain_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.domain_update(
        domain_update=domain_update,
        domain=domain,
        session=session,
    )


@gods_router.delete("/domain_delete/{domain_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def domain_delete(
        domain: models.Domain = Depends(dependencies.get_domain_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    await crud.domain_delete(domain=domain, session=session)
