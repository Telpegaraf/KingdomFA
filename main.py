from contextlib import asynccontextmanager
from fastapi import FastAPI

from api_v1.routers import domain

app = FastAPI()
app.include_router(domain.domain_router)
app.include_router(domain.domain_router)


@asynccontextmanager
async def lifespan(app: FastAPI):
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
# def create_domain(god: schemas.DomainBase, db: Session = Depends(get_db)):
#     return crud.create_domain(db=db, god=god)
#
#
# @app.get("/domain/", response_model=List[schemas.God])
# def read_gods(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#     domain = db.query(models.God).offset(skip).limit(limit).all()
#     return domain

