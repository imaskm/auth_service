from pydantic import BaseModel


class Email(BaseModel):
    email_content: str
    email_id: str