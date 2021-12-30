import re
from flask import render_template

from flaskr.constants import EMAIL_REGEX


def apology(message, code=400):
    """Render message as an apology to user.
    """

    def escape(s):
        """
        Escape special characters.
        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s

    return render_template("errors/apology.html", top=code, bottom=escape(message)), code


def is_valid_email(email):
    if re.fullmatch(EMAIL_REGEX, email) is None:
        raise ValueError('Not a valid email address')
    else:
        return email

