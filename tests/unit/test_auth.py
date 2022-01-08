"""Unit tests for the classes used to store the db models"""
import unittest

from flaskr.app import create_app
from flaskr.labels import messages


# pylint: disable=missing-function-docstring
from flaskr.models.user import User


class TestLogin(unittest.TestCase):
    """Unit tests for the login functionality"""

    def setUp(self):
        self.app = create_app(config='config.TestConfig')
        self.context = self.app.app_context()
        self.context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.context.pop()
        self.app = None
        self.context = None
        self.client = None

    def test_login_form_contains_correct_fields(self):
        response = self.client.get('/login')
        self.assertEqual(200, response.status_code)

        html = response.get_data(as_text=True)
        # make sure the input fields are included
        self.assertIn('name="username"', html)
        self.assertIn('name="password"', html)

    def test_login_form_menu_only_contains_login_and_register_menu_items(self):
        response = self.client.get('/login')
        self.assertEqual(200, response.status_code)

        html = response.get_data(as_text=True)
        # make sure the input fields are included
        self.assertNotIn('href="/account">Account', html)
        self.assertNotIn('href="/game">Game', html)
        self.assertNotIn('href="/logout">Logout', html)
        self.assertIn('href="/register">Register', html)
        self.assertIn('href="/login">Log In', html)

    def test_home_page_redirect_with_no_current_user_redirects_to_login(self):
        response = self.client.get('/', follow_redirects=True)
        self.assertEqual('/login', response.request.path)

    # This should be improved using mocking of the database rather than using actual values in the real database
    def test_home_page_redirect_with_current_user_redirects_to_account(self):
        with self.client:
            #  given
            data = dict(username='WhiteFamily', password='bluesky')
            self.client.post('/login', data=data)
            # when
            response = self.client.get('/', follow_redirects=True)
            # then
            self.assertEqual('/account', response.request.path)

    def test_login_with_empty_form_flashes_incorrect_details_message(self):
        data = dict(username="", password="")
        response = self.client.post('/login', data=data, follow_redirects=True)
        self.assertIn(bytes(messages.INCORRECT_DETAILS, encoding='utf-8'), response.data)

    def test_login_with_no_password_flashes_incorrect_details_message(self):
        data = dict(username="WhiteFamily", password="")
        response = self.client.post('/login', data=data, follow_redirects=True)
        self.assertIn(bytes(messages.INCORRECT_DETAILS, encoding='utf-8'), response.data)

    def test_login_with_no_username_flashes_incorrect_details_message(self):
        data = dict(username="", password="password")
        response = self.client.post('/login', data=data, follow_redirects=True)
        self.assertIn(bytes(messages.INCORRECT_DETAILS, encoding='utf-8'), response.data)


# pylint: disable=missing-function-docstring
class TestRegister(unittest.TestCase):
    """Unit tests for the login and registration functionality"""

    def setUp(self):
        self.app = create_app(config='config.TestConfig')
        self.context = self.app.app_context()
        self.context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.context.pop()
        self.app = None
        self.context = None
        self.client = None

    def test_registration_form_contains_correct_fields(self):
        response = self.client.get('/register')
        self.assertEqual(200, response.status_code)

        html = response.get_data(as_text=True)
        # make sure the input fields are included
        self.assertIn('name="username"', html)
        self.assertIn('name="password"', html)
        self.assertIn('name="confirm_password"', html)
        self.assertIn('name="f_name"', html)
        self.assertIn('name="surname"', html)
        self.assertIn('name="email"', html)

    def test_registration_form_menu_only_contains_login_and_register_menu_items(self):
        response = self.client.get('/register')
        self.assertEqual(200, response.status_code)

        html = response.get_data(as_text=True)
        # make sure the input fields are included
        self.assertNotIn('href="/account">Account', html)
        self.assertNotIn('href="/game">Game', html)
        self.assertNotIn('href="/logout">Logout', html)
        self.assertIn('href="/register">Register', html)
        self.assertIn('href="/login">Log In', html)

    def test_register_with_empty_form_flashes_all_fields_required_message(self):
        data = dict(username="", password="", confirm_password="", f_name="", surname="", email="")
        response = self.client.post('/register', data=data, follow_redirects=True)
        self.assertIn(bytes(messages.ALL_FIELDS_REQUIRED, encoding='utf-8'), response.data)

    def test_register_with_one_field_missing_flashes_all_fields_required_message(self):
        data = dict(username="name", password="password", confirm_password="password", f_name="a",
                    surname="user", email="")
        response = self.client.post('/register', data=data, follow_redirects=True)
        self.assertIn(bytes(messages.ALL_FIELDS_REQUIRED, encoding='utf-8'), response.data)

    def test_register_with_password_not_confirmed_flashes_non_matching_password_message(self):
        data = dict(username="username", password="password", confirm_password="wrong password", f_name="a",
                    surname="user", email="user@user.com")
        response = self.client.post('/register', data=data, follow_redirects=True)
        self.assertIn(bytes(messages.NON_MATCHING_PASSWORD, encoding='utf-8'), response.data)

    def test_register_with_invalid_password_flashes_invalid_password_message(self):
        data = dict(username="User", password="1", confirm_password="1", f_name="a",
                    surname="user", email="user@user.com")
        response = self.client.post('/register', data=data, follow_redirects=True)
        self.assertIn(bytes(messages.INVALID_PASSWORD, encoding='utf-8'), response.data)

    def test_register_with_invalid_email_flashes_invalid_email_message(self):
        data = dict(username="User", password="password", confirm_password="password", f_name="a",
                    surname="user", email="invalid_email")
        response = self.client.post('/register', data=data, follow_redirects=True)
        self.assertIn(bytes(messages.INVALID_EMAIL_ADDRESS, encoding='utf-8'), response.data)


# pylint: disable=missing-function-docstring
class TestLogout(unittest.TestCase):
    """Unit tests for the login and registration functionality"""

    def setUp(self):
        self.app = create_app(config='config.TestConfig')
        self.context = self.app.app_context()
        self.context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.context.pop()
        self.app = None
        self.context = None
        self.client = None

    def test_logout_redirects_to_login(self):
        response = self.client.get('/logout', follow_redirects=True)
        self.assertEqual(200, response.status_code)
        self.assertEqual('/login', response.request.path)


if __name__ == '__main__':
    unittest.main()
