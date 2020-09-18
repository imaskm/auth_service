from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from routers.token_endpoints import oauth2_scheme
from operations import token_operations, confirm_email_operations
from database import crud_users
import db_dep

email_confirm_router = APIRouter()


@email_confirm_router.post("/sendconfirmemail/")
async def send_email(*, token: str = Depends(oauth2_scheme), db: Session = Depends(db_dep.get_db), request: Request):
    token_username = token_operations.get_username_from_token(token)
    user = crud_users.get_user_by_username(token_username, db)

    if user.is_confirmed:
        return {"message" : "Email already confirmed"}
    import pdb
    pdb.set_trace()
    await confirm_email_operations.send_confirmation_email(user.username, user.email, request.base_url)
    return {"message": "A confirmation email has been sent to your email id, please check your emails"}

