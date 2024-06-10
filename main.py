from fastapi import FastAPI

from apps.gods import models, views
from database import engine

app = FastAPI()
app.include_router(views.gods_router)

models.Base.metadata.create_all(bind=engine)


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

