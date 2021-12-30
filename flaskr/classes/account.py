from sqlalchemy import Column, String, Integer

from flaskr.classes.base import Base

from flaskr.helpers.helpers import is_valid_email


class Account(Base):
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    hash = Column(String)
    f_name = Column(String)
    surname = Column(String)
    email = Column(String)

    def __init__(self, username, hash, f_name, surname, email):
        self.username = username
        self.hash = hash
        self.f_name = f_name
        self.surname = surname
        self.email = is_valid_email(email)
