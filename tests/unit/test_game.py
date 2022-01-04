"""Unit tests for the classes used to store the db models"""
import unittest

from flaskr.app import create_app


# pylint: disable=missing-function-docstring
class TestAccount(unittest.TestCase):
    """Unit tests for the game page and functionality"""

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

    def test_game_route_with_no_user_logged_in_redirects_to_login_page(self):
        response = self.client.get('/game', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.request.path, '/login')