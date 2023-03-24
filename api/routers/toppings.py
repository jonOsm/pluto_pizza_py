from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schema.toppings_schema import Topping
from api.crud.toppings_crud import read_toppings
from db.setup import get_db

router = APIRouter(prefix="/toppings", tags=["toppings"])


@router.get("/")
def index(db: Session = Depends(get_db)) -> list[Topping]:
    return read_toppings(db)
