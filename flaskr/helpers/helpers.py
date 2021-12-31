import re
from flaskr.constants import EMAIL_REGEX
from flaskr.errors.errors import InvalidEmailError
from flaskr.labels import messages


def is_valid_email(email):
    if re.fullmatch(EMAIL_REGEX, email) is None:
        raise InvalidEmailError(messages.INVALID_EMAIL_ADDRESS)
    else:
        return email

