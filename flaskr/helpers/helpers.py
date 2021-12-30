import re
from flaskr.constants import EMAIL_REGEX


def is_valid_email(email):
    if re.fullmatch(EMAIL_REGEX, email) is None:
        raise ValueError('Not a valid email address')
    else:
        return email

