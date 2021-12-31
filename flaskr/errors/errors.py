
class Error(Exception):
    """Base class for other exceptions"""
    pass


class InvalidEmailError(Error):
    pass


class InvalidPasswordError(Error):
    pass
