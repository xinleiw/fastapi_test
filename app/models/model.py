from sqlalchemy import Column, Integer, String

from .database import Base


class Model(Base):
    __tablename__ = "model"
    id = Column(Integer, primary_key=True, index=True)
    department = Column(String)
    name = Column(String)
    path = Column(String)
    type = Column(String)
