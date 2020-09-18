from database.base import Base
from sqlalchemy import Integer,String, Column


class blo(Base):
    __tablename__ = "products"

    product_id = Column(String)
    product_name = Column(String)