from passlib.context import CryptContext

PASSWORD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_hashed_password(password: str) -> any:
    return PASSWORD_CONTEXT.hash(password)


def verify_password(password,db_password) -> bool:
    return PASSWORD_CONTEXT.verify(password,db_password)
