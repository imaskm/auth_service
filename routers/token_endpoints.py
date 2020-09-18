from datetime import timedelta
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.token_schema import Token
from database import crud_users
from operations import token_operations
import db_dep, settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/authentication")

auth_router = APIRouter()


@auth_router.post("/authentication", response_model=Token)
def get_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(db_dep.get_db)):
    if not crud_users.check_username_password(form_data.username, form_data.password, db):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid credentials")

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = token_operations.create_access_token(data={"sub": form_data.username, "scope": "user"},
                                                        expires_delta=access_token_expires)

    return {"access_token": access_token, "token_type": "Bearer"}
