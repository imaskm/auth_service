from schemas.users import UserCreate
from sqlalchemy.orm import Session
import re, email_validator
from fastapi import HTTPException, status


def is_valid_username(username: str):
    username_regex = "^[a-z][a-z0-9]{4,16}$"
    return re.match(username_regex,username)


def is_valid_email(email: str):
    try:
        email_validator.validate_email(email)
    except email_validator.EmailNotValidError:
        return False
    return True


def validate_user(user: UserCreate):
    if not is_valid_username(user.username):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Invalid username, username must be of length 4 to 16 ")
    if not is_valid_email(user.email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Invalid email id")
    return True


