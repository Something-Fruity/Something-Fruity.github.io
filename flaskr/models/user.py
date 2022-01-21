"""Defines a user class mapped to the user table in the database"""

from sqlalchemy import Column, String, Integer, DateTime
from werkzeug.security import check_password_hash, generate_password_hash

from flask_login import UserMixin

from flaskr.models.base import Base
from flaskr.helpers.helpers import is_valid_email, is_valid_password


class User(UserMixin, Base):  # pylint: disable=too-few-public-methods
    """Holds the account details for an individual: username and password,
        and date of last login."""

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    hash = Column(String)
    f_name = Column(String)
    surname = Column(String)
    email = Column(String)
    last_login = Column(DateTime, index=False, unique=False, nullable=True)
    language = Column(String)

    # pylint: disable=too-many-arguments
    def __init__(self, username, password, f_name, surname, email, last_login, language):
        self.username = username
        self.set_password(is_valid_password(password))
        self.f_name = f_name
        self.surname = surname
        self.email = is_valid_email(email)
        self.last_login = last_login
        self.language = language

    def set_password(self, password):
        """Create hashed password."""
        self.hash = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.hash, password)
