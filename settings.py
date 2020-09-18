from fastapi import HTTPException, status
import os
# constants
SECRET_KEY = os.environ['JWT_SECRET_KEY']
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# exceptions
CREDENTIAL_EXCEPTION = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid Credentials",
    headers={"WWW-Authenticate": "Bearer"}
)

ACCESS_EXCEPTION = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Not Authorized to access this page",
    headers={"WWW-Authenticate": "Bearer"}
)

NOT_CONFIRMED_EXCEPTION = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Email not yet confirmed"
)

CONFIRMATION_TOKEN_EXPIRED = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="This confirmation email is expired, please go to home page and initiate a new email"
)

CONFIRM_EMAIL_BODY = "Please click on following link to confirm you email \n"
CONFIRM_EMAIL_SUBJECT = "Confirm Email"
# mail settings
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_SERVICE = "gmail"
# gmail authentication
EMAIL_ID = os.environ['EMAIL_ID']
EMAIL_PASSWORD = os.environ['EMAIL_PASSWORD']

CONFIRMATION_TOKEN_SECRET_KEY = 'secretkey'
CONFIRMATION_TOKEN_SECURITY_SALT = 'secretpasswordsalt'
CONFIRMATION_TOKEN_MAX_AGE = 300
