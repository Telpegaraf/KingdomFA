from fastapi import HTTPException
from sqlalchemy.orm import Session
from apps.gods import models, schemas


def domain_detail(domain_id: int, db: Session):
    domain = db.query(models.Domain).filter(models.Domain.id == domain_id).first()
    if not domain:
        raise HTTPException(status_code=404, detail="Domain isn't found")
    return domain


def create_domain(domain: schemas.DomainBase, db: Session):
    db_domain = models.Domain(name=domain.name)
    db.add(db_domain)
    db.commit()
    db.refresh(db_domain)
    return db_domain


def domain_list(db: Session):
    return db.query(models.Domain).all()
