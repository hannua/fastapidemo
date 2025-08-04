from sqlalchemy.orm import Session
from . import crud, schemas
from app.core.database import SessionLocal

def get_all_users():
    db: Session = SessionLocal()
    try:
        return crud.get_all_users(db)
    finally:
        db.close()


