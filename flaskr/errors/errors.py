"""Defining errors and exceptions"""


class Error(Exception):
    """Base class for other exceptions"""


class InvalidEmailError(Error):
    """For invalid emails"""


class InvalidPasswordError(Error):
    """For invalid passwords"""
