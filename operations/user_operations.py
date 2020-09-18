from utils import validations
from schemas.users import UserCreate
from sqlalchemy.orm import Session


def check_if_user_is_valid(user: UserCreate, db: Session):
    return validations.validate_user(user)
