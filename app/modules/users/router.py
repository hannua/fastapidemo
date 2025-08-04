from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from . import schemas, crud

router = APIRouter()

@router.post("/", response_model=schemas.UserOut)
def create(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@router.get("/", response_model=list[schemas.UserOut])
def list_users(db: Session = Depends(get_db)):
    return crud.get_users(db)
