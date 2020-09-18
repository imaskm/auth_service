from sqlalchemy import Column,Integer,String, Boolean, DateTime
from database.base import Base


class User(Base):
    __tablename__ = "users"

    username = Column(String, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String)
    is_active = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
    is_confirmed = Column(Boolean, default=False)
    confirmed_on = Column(DateTime)




