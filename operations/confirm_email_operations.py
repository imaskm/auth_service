from fastapi_mail import FastMail
import settings
from itsdangerous import URLSafeTimedSerializer


async def send_confirmation_email(username: str, email: str, baseurl):
    mail = FastMail(
        email=settings.EMAIL_ID,
        password=settings.EMAIL_PASSWORD,
        tls=settings.EMAIL_USE_TLS,
        port=settings.EMAIL_PORT,
        service=settings.EMAIL_SERVICE
    )
    token = get_confirmation_token_from_username(username)
    try:
        await mail.send_message(
            recipient=email,
            subject=settings.CONFIRM_EMAIL_SUBJECT,
            body=f"Hi {username}, {settings.CONFIRM_EMAIL_BODY}\n\n {baseurl}confirm/{token}",
            text_format="html"
        )
    except:
        raise Exception("Invalid")

    return True


def get_confirmation_token_from_username(username) -> str:
    serializer = URLSafeTimedSerializer(settings.CONFIRMATION_TOKEN_SECRET_KEY)
    return serializer.dumps(username, salt=settings.CONFIRMATION_TOKEN_SECURITY_SALT)


def get_username_from_confirmation_token(token):
    serializer = URLSafeTimedSerializer(settings.CONFIRMATION_TOKEN_SECRET_KEY)
    try:
        username = serializer.loads(
            token,
            salt=settings.CONFIRMATION_TOKEN_SECURITY_SALT,
            max_age=settings.CONFIRMATION_TOKEN_MAX_AGE
        )
    except:
        raise settings.CONFIRMATION_TOKEN_EXPIRED

    return username
