from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session

from app.deps import get_db
from app.crud import model
from app.models.model import Model
router = APIRouter()


@router.post("/")
def create_product(db: Session = Depends(get_db), name=Body(None)):
    model_abj = model.add_model(db, name)
    return model_abj

@router.get("/")
def get_product(db: Session = Depends(get_db)):
    model_abj = model.get_model(db)
    return model_abj
