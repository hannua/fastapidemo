from fastapi import APIRouter , Depends
from . import schemas, services


router = APIRouter()

@router.get("/")
def list_items():
    return services.get_all_items()
