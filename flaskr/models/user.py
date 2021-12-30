from sqlalchemy import Column, String, Integer, DateTime
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.models.base import Base
from flask_login import UserMixin

from flaskr.helpers.helpers import is_valid_email


class User(UserMixin, Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    hash = Column(String)
    f_name = Column(String)
    surname = Column(String)
    email = Column(String)
    last_login = Column(DateTime, index=False, unique=False, nullable=True)

    def __init__(self, username, hash, f_name, surname, email, last_login):
        self.username = username
        self.hash = hash
        self.f_name = f_name
        self.surname = surname
        self.email = is_valid_email(email)
        self.last_login = last_login

    def set_password(self, password):
        """Create hashed password."""
        self.hash = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.hash, password)
