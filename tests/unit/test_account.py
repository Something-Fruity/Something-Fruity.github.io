"""Unit tests for the classes used to store the db models"""
from flask_testing import TestCase

from flaskr.app import create_app


# pylint: disable=missing-function-docstring
class TestAccount(TestCase):
    """Unit tests for the account page and functionality"""

    def create_app(self):
        return create_app(config='config.TestConfig')

    def test_account_route_with_no_user_logged_in_redirects_to_login_page(self):
        response = self.client.get('/account', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.request.path, '/login')

    def test_account_route_with_user_logged_in_renders_account_template(self):
        # given
        data = dict(username='WhiteFamily', password='bluesky')
        self.client.post('/login', data=data)
        # when
        response = self.client.get('/account', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('account.html')

    def test_delete_account_deletes_account_displays_message_and_redirects_to_login_page(self):
        pass
        # # given
        #
        # # when
        # self.client.form = 'delete'
        # response = self.client.post('/account', follow_redirects=True)
        # # then
        # self.assertEqual(response.status_code, 200)
        # self.assert_template_used('login.html')
