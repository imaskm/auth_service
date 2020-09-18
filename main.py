from fastapi import FastAPI
from routers.users import router as user_router
from routers.token_endpoints import auth_router
from routers.confirm_email import email_confirm_router
from database import base

base.Base.metadata.create_all(bind=base.engine)

app = FastAPI()

app.include_router(
    user_router,
    prefix="/user",
    tags=["user"]
    )

app.include_router(
    auth_router,
    tags=["auth"]
    )

app.include_router(
    email_confirm_router,
    tags=["email confirmation"]

)






