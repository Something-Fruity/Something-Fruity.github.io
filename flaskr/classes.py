import re

from flaskr.constants import EMAIL_REGEX


def is_valid_email(email):
    if re.fullmatch(EMAIL_REGEX, email) is None:
        raise ValueError('Not a valid email address')
    else:
        return email


class Account:
    def __init__(self, *args):
        if len(args) == 1:   # all parameters were passed in as list
            params = args[0]
            self._id = params[0]
            self.username = params[1]
            self.hash = params[2]
            self.f_name = params[3]
            self.surname = params[4]
            self.email = is_valid_email(params[5])

        else:   # parameters were passed individually
            self.username = args[0]
            self.hash = args[1]
            self.f_name = args[2]
            self.surname = args[3]
            self.email = is_valid_email(args[4])

    @property
    def id(self):
        return self._id

    def get_details(self):
        details = []
        details.extend([self.username, self.hash, self.f_name, self.surname, self.email])
        return details

    def __repr__(self):
        return f'(id: {self.id} \nusername: {self.username}\nfirst name: {self.f_name} \nsurname: {self.surname}' \
               f'\nemail: {self.email}) '





