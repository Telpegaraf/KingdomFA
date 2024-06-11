from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from functools import lru_cache

from api_v1.gods import models, views
from core.models import Base
from database import db_helper

app = FastAPI()
app.include_router(views.gods_router)


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield

# @app.on_event("startup")
# async def on_startup():
#     async with engine.begin() as conn:
#         await conn.run_sync(models.Base.metadata.create_all)


#models.Base.metadata.create_all(bind=engine)


# @app.get("/domains/", response_model=List[schemas.Domain])
# def read_domains(db: Session = Depends(get_db)):
#     domains = crud.get_all_domains(db)
#     return domains
#
#
# @app.post("/domains/", response_model=schemas.Domain)
# def create_domain(domain: schemas.DomainBase, db: Session = Depends(get_db)):
#     return crud.create_domain(db=db, domain=domain)
#
#
# @app.get("/gods/", response_model=List[schemas.God])
# def read_gods(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#     gods = db.query(models.God).offset(skip).limit(limit).all()
#     return gods

