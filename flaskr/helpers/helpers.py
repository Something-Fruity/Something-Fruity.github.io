import re
from flaskr.constants import EMAIL_REGEX
from flaskr.errors.errors import InvalidEmailError, InvalidPasswordError
from flaskr.labels import messages


def is_valid_email(email):
    if re.fullmatch(EMAIL_REGEX, email) is None:
        raise InvalidEmailError(messages.INVALID_EMAIL_ADDRESS)
    else:
        return email


def is_valid_password(password):
    if len(password) < 6:
        raise InvalidPasswordError(messages.INVALID_PASSWORD)
    else:
        return password
