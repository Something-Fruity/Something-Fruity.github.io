"""Unit tests for the classes used to store the db models"""

from flask_testing import TestCase
from flaskr.app import create_app


# pylint: disable=missing-function-docstring
class TestGame(TestCase):
    """Unit tests for the game page and functionality"""

    def create_app(self):
        return create_app(config='config.TestConfig')

    def test_game_route_with_no_user_logged_in_redirects_to_login_page(self):
        response = self.client.get('/game', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.request.path, '/login')

    def test_game_route_with_user_logged_in_renders_game_template(self):
        # given
        data = dict(username='WhiteFamily', password='bluesky')
        self.client.post('/login', data=data)
        # when
        response = self.client.get('/game', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('game.html')
