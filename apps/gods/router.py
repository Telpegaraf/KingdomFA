from fastapi import HTTPException, APIRouter

from apps.gods import models, schemas
from database import dp_dependency


gods_router = APIRouter(prefix="/gods")


@gods_router.get("/domain/{domain_id}")
async def domain_detail(domain_id: int, db: dp_dependency):
    result = db.query(models.Domain).filter(models.Domain.id == domain_id).first()
    if not result:
        raise HTTPException(status_code=404, detail="Domain isn't found")
    return result


@gods_router.post("/domain/")
async def create_domain(domain: schemas.DomainBase, db: dp_dependency):
    db_domain = models.Domain(name=domain.name)
    db.add(db_domain)
    db.commit()
    db.refresh(db_domain)


@gods_router.get("/domain_list/")
async def domain_list(db: dp_dependency):
    result = db.query(models.Domain).all()
    return result

