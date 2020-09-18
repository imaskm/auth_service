from fastapi import APIRouter, Depends, Path, HTTPException, status
from schemas.users import User, UserCreate, UserUpdate
from sqlalchemy.orm import Session
from database import crud_users
from operations import user_operations
from routers.token_endpoints import oauth2_scheme
from operations import token_operations
from routers.confirm_email import email_confirm_router
import db_dep, settings

router = APIRouter()


@router.post("/", response_model=User)
def add_user(user: UserCreate, db: Session = Depends(db_dep.get_db)):
    user_operations.check_if_user_is_valid(user, db)
    crud_users.check_if_user_details_already_used(user, db)
    import pdb
    pdb.set_trace()
    email_confirm_router.post("/sendconfirmemail/")
    return crud_users.create_user(user, db)


@router.get("/{username}", response_model=User)
def get_user(username: str, token: str = Depends(oauth2_scheme), db: Session = Depends(db_dep.get_db)):

    token_username = token_operations.get_username_from_token(token)
    if username != token_username:
        raise settings.ACCESS_EXCEPTION

    user = crud_users.get_user_by_username(token_username, db)
    if not user:
        raise settings.CREDENTIAL_EXCEPTION

    if not user.is_confirmed:
        raise settings.NOT_CONFIRMED_EXCEPTION

    return user


@router.put("/{username}", response_model=User)
def update_user(
        *,
        user: UserUpdate,
        username: str,
        token: str = Depends(oauth2_scheme),
        db: Session = Depends(db_dep.get_db)
        ):
    
    token_username = token_operations.get_username_from_token(token)

    if username != token_username:
        raise settings.ACCESS_EXCEPTION

    updated_user = crud_users.update_user(username, user, db)
    return updated_user




