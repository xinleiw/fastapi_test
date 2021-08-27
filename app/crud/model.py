from app.models.model import Model
from sqlalchemy.orm import Session


def add_model(db: Session, model_info: dict):
    model = Model()
    model.department = model_info.get("department")
    model.name = model_info.get("name")
    model.path = model_info.get("path")
    model.type = model_info.get("type")
    db.add(model)
    db.commit()
    db.refresh(model)
    return model


def get_model(db: Session):
    model = db.query(Model).all()
    return model
