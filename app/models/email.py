'''This module contains all email related models'''

from enum import Enum, unique
from email.headerregistry import Address

from pydantic import BaseModel, EmailStr


class EmailAddress(BaseModel):
    email: EmailStr


class EmailMsg(BaseModel):
    recipient: Address
    subject: str
    text: str
    html: str

    class Config:
        '''Pydantic config'''
        arbitrary_types_allowed = True


@unique
class EmailSecurity(Enum):
    '''Security options for SMTP'''
    TLS_SSL = 'tls_ssl'
    STARTTLS = 'starttls'
    UNSECURE = 'unsecure'
