from fastapi import APIRouter

from apps.gods import models, schemas, crud
from database import dp_dependency


gods_router = APIRouter(prefix="/gods")


@gods_router.get("/domain/{domain_id}")
async def domain_detail(domain_id: int, db: dp_dependency):
    result = crud.domain_detail(domain_id=domain_id, db=db)
    return result


@gods_router.post("/domain/")
async def create_domain(domain: schemas.DomainBase, db: dp_dependency):
    result = crud.create_domain(domain=domain, db=db)
    return result


@gods_router.get("/domain_list/")
async def domain_list(db: dp_dependency):
    result = crud.domain_list(db=db)
    return result
