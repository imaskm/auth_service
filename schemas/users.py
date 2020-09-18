from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True


class UserCreate(User):
    password: str

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    email: str
    password : str
    new_password: str

    class Config:
        orm_mode = True
    
