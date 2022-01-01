"""Contains public helper methods that can be imported and accessed from
    anywhere in the application."""

import re

from flaskr.constants import EMAIL_REGEX
from flaskr.errors.errors import InvalidEmailError, InvalidPasswordError
from flaskr.labels import messages


def is_valid_email(email):
    """checks an email is constructed correctly
        returns the email or
        raises an InvalidEmailError"""
    if re.fullmatch(EMAIL_REGEX, email) is None:
        raise InvalidEmailError(messages.INVALID_EMAIL_ADDRESS)
    return email


def is_valid_password(password):
    """checks a password is constructed correctly
        returns the password or
        raises an InvalidPasswordError"""
    if len(password) < 6:
        raise InvalidPasswordError(messages.INVALID_PASSWORD)
    return password
