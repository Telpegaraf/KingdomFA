from fastapi import APIRouter, status, Depends
from fastapi.security import HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.crud import religion as crud
from api_v1.dependencies.get_object import get_object_by_id_dependency
from api_v1.models.religion import Domain, God
from api_v1.schemas import religion as schemas
from auth.utils import get_current_token_payload
from database import db_helper

http_bearer = HTTPBearer(auto_error=False)

religion_router = APIRouter(prefix="/domain", tags=["Domains"], dependencies=[Depends(http_bearer)])


@religion_router.get(
    "/{object_id}/",
    description="Return the domain object, depending on ID",
    response_model=schemas.Domain
)
async def domain_detail(
        payload: dict = Depends(get_current_token_payload),
        domain: Domain = Depends(get_object_by_id_dependency(Domain))
):
    return domain


@religion_router.get(
    "/",
    description="Return all domain objects",
    response_model=list[schemas.Domain]
)
async def domain_list(
        payload: dict = Depends(get_current_token_payload),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    result = await crud.domain_list(session=session)
    return result


@religion_router.post(
    "/create/",
    description="Create a new Domain object",
    response_model=schemas.Domain,
    status_code=status.HTTP_201_CREATED
)
async def domain_create(
        domain_in: schemas.DomainBase,
        payload: dict = Depends(get_current_token_payload),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    result = await crud.domain_create(domain_in=domain_in, session=session)
    return result


@religion_router.patch(
    "/update/{object_id}/",
    response_model=schemas.Domain,
    description="Update a Domain object, depending on ID"
)
async def domain_update(
        domain_update: schemas.DomainUpdate,
        payload: dict = Depends(get_current_token_payload),
        domain: Domain = Depends(get_object_by_id_dependency(Domain)),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.domain_update(
        domain_update=domain_update,
        domain=domain,
        session=session,
    )


@religion_router.delete(
    "/delete/{object_id}/",
    description="Delete a Domain object, depending on ID",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def domain_delete(
        payload: dict = Depends(get_current_token_payload),
        domain: Domain = Depends(get_object_by_id_dependency(Domain)),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    await crud.domain_delete(domain=domain, session=session)
    

@religion_router.get("/{object_id}/")
async def god_detail(
        payload: dict = Depends(get_current_token_payload),
        god: God = Depends(get_object_by_id_dependency(God))
):
    return god


@religion_router.get("/", response_model=list[schemas.God])
async def god_list(
        payload: dict = Depends(get_current_token_payload),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    result = await crud.god_list(session=session)
    return result


@religion_router.post("/create/", status_code=status.HTTP_201_CREATED)
async def god_create(
        god_in: schemas.GodBase,
        payload: dict = Depends(get_current_token_payload),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    result = await crud.god_create(god_in=god_in, session=session)
    return result


@religion_router.patch("/update/{object_id}/")
async def update(
        god_update: schemas.GodBase,
        payload: dict = Depends(get_current_token_payload),
        god: God = Depends(get_object_by_id_dependency(God)),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.god_update(
        god_update=god_update,
        god=god,
        session=session
    )


@religion_router.delete("/delete/{object_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(
        payload: dict = Depends(get_current_token_payload),
        god: God = Depends(get_object_by_id_dependency(God)),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    await crud.god_delete(god=god, session=session)
    
