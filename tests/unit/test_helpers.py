import unittest

from flaskr.errors.errors import InvalidEmailError
from flaskr.helpers.helpers import is_valid_email
from flaskr.labels import messages


class TestHelpers(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
