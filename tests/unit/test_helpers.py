import unittest

from flaskr.errors.errors import InvalidEmailError, InvalidPasswordError
from flaskr.helpers.helpers import is_valid_email, is_valid_password
from flaskr.labels import messages


class TestEmailHelper(unittest.TestCase):
    def test_is_valid_email_with_valid_email_returns_email(self):
        # given
        email = 'walter@white.com'
        # when
        result = is_valid_email(email)
        # then
        self.assertEqual(email, result)

    def test_is_valid_email_with_valid_email_containing_more_than_one_full_stop_returns_email(self):
        # given
        email = 'walter@white.com'
        # when
        result = is_valid_email(email)
        # then
        self.assertEqual(email, result)

    def test_is_valid_email_with_valid_email_containing_underscores_returns_email(self):
        # given
        email = 'walter_white@white.com'
        # when
        result = is_valid_email(email)
        # then
        self.assertEqual(email, result)

    def test_is_valid_email_with_valid_email_containing_numbers_returns_email(self):
        # given
        email = 'walter99@white.com'
        # when
        result = is_valid_email(email)
        # then
        self.assertEqual(email, result)

    def test_is_valid_email_with_valid_email_containing_all_CAPS_returns_email(self):
        # given
        email = 'WALTER@WHITE.COM'
        # when
        result = is_valid_email(email)
        # then
        self.assertEqual(email, result)

    def test_is_valid_email_with_email_missing_at_sign_raises_InvalidEmailError(self):
        # given
        email = 'walterwhite.com'
        # when
        try:
            is_valid_email(email)
        # then
        except InvalidEmailError as e:
            self.assertEqual(type(e), InvalidEmailError)
            self.assertEqual(messages.INVALID_EMAIL_ADDRESS, str(e))
        else:
            self.fail('InvalidEmailError not raised')

    def test_is_valid_email_with_email_missing_chars_before_at_sign_raises_InvalidEmailError(self):
        # given
        email = '@white.com'
        # when
        try:
            is_valid_email(email)
        # then
        except InvalidEmailError as e:
            self.assertEqual(type(e), InvalidEmailError)
            self.assertEqual(messages.INVALID_EMAIL_ADDRESS, str(e))
        else:
            self.fail('InvalidEmailError not raised')

    def test_is_valid_email_with_email_missing_chars_after_at_sign_raises_InvalidEmailError(self):
        # given
        email = 'walter@'
        # when
        try:
            is_valid_email(email)
        # then
        except InvalidEmailError as e:
            self.assertEqual(type(e), InvalidEmailError)
            self.assertEqual(messages.INVALID_EMAIL_ADDRESS, str(e))
        else:
            self.fail('InvalidEmailError not raised')

    def test_is_valid_email_with_email_missing_full_stop_raises_InvalidEmailError(self):
        # given
        email = 'walter@whitecom'
        # when
        try:
            is_valid_email(email)
        # then
        except InvalidEmailError as e:
            self.assertEqual(type(e), InvalidEmailError)
            self.assertEqual(messages.INVALID_EMAIL_ADDRESS, str(e))
        else:
            self.fail('InvalidEmailError not raised')

    def test_is_valid_email_with_email_missing_chars_after_full_stop_raises_InvalidEmailError(self):
        # given
        email = 'walter@white.'
        # when
        try:
            is_valid_email(email)
        # then
        except InvalidEmailError as e:
            self.assertEqual(type(e), InvalidEmailError)
            self.assertEqual(messages.INVALID_EMAIL_ADDRESS, str(e))
        else:
            self.fail('InvalidEmailError not raised')


class TestPasswordHelper(unittest.TestCase):
    def test_is_valid_password_with_valid_password_returns_password(self):
        # given
        password = 'password'
        # when
        result = is_valid_password(password)
        # then
        self.assertEqual(password, result)

    def test_is_valid_password_with_valid_password_containing_numbers_returns_password(self):
        # given
        password = '1234556'
        # when
        result = is_valid_password(password)
        # then
        self.assertEqual(password, result)

    def test_is_valid_password_with_valid_password_containing_mix_of_letters_and_numbers_returns_password(self):
        # given
        password = 'A1a2B3q4x55p6'
        # when
        result = is_valid_password(password)
        # then
        self.assertEqual(password, result)

    def test_is_valid_password_with_short_password_raises_InvalidPasswordError(self):
        # given
        password = '12345'
        # when
        try:
            is_valid_password(password)
        # then
        except InvalidPasswordError as e:
            self.assertEqual(type(e), InvalidPasswordError)
            self.assertEqual(messages.INVALID_PASSWORD, str(e))
        else:
            self.fail('InvalidPasswordError not raised')

    def test_is_valid_password_with_empty_string_raises_InvalidPasswordError(self):
        # given
        password = ''
        # when
        try:
            is_valid_password(password)
        # then
        except InvalidPasswordError as e:
            self.assertEqual(type(e), InvalidPasswordError)
            self.assertEqual(messages.INVALID_PASSWORD, str(e))
        else:
            self.fail('InvalidPasswordError not raised')


if __name__ == '__main__':
    unittest.main()
