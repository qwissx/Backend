from barbeshop.db.db_connect import Base
from sqlalchemy import Column, Integer

class BaseModel(Base):
    __abstract__ = True
    __allow_unmapped__ = True

    id = Column(Integer, primary_key=True)