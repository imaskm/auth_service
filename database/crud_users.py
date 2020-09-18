from sqlalchemy.orm import Session
from models.users import User
from schemas.users import UserCreate, UserUpdate
from utils import securities, validations

from fastapi import HTTPException, status


def check_if_username_exists(username: User.username, db: Session):
    return db.query(User).filter(User.username == username).first()


def check_if_email_exists(email: User.email, db: Session):
    return db.query(User).filter(User.email == email).first()


def get_user_by_username(username: User.username, db: Session) -> User:
    return db.query(User).filter(User.username == username).first()


def create_user(user: UserCreate, db: Session):
    user.password = securities.get_hashed_password(user.password)
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def check_if_user_details_already_used(user: UserUpdate, db):
    if check_if_username_exists(user.username, db):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="username already taken")
    if check_if_email_exists(user.email, db):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="email already exists")

    return True


def update_user(username, user: UserUpdate, db: Session):
    if not check_username_password(username, user.password, db):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid password")
    db_user = get_user_by_username(username, db)

    if user.email != db_user.email:
        if not validations.is_valid_email(user.email):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Invalid email id")

        if check_if_email_exists(user.email, db):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="email already exists")

    user.password = securities.get_hashed_password(user.password)
    updated_user = UserCreate(**user.dict(), username=username)
    for key, value in updated_user.dict(exclude_unset=True).items():
        setattr(db_user, key, value)

    if user.new_password:
        db_user.password = securities.get_hashed_password(user.new_password)

    db.commit()
    db.refresh(db_user)
    return db_user


def check_username_password(username: User.username, password: User.password, db: Session):
    db_user = get_user_by_username(username, db)
    if db_user:
        return securities.verify_password(password, db_user.password)
