"""Unit tests for the classes used to store the db models"""
import unittest
from datetime import date

from flaskr.errors.errors import InvalidEmailError
from flaskr.models.user import User
from flaskr.models.player import Player
from flaskr.models.persona import Persona
from flaskr.models.game import Game

from flaskr.labels import messages


def create_test_user():
    """Create and return a user"""
    return User('heisenberg', 'my-password', 'walter', 'white', 'walter@white.com', date.today())


# pylint: disable=missing-function-docstring
class TestModels(unittest.TestCase):
    """Unit tests for the classes used to store the db models"""
    def test_create_new_user_returns_user(self):
        # given
        test_user = None

        # when
        test_user = create_test_user()

        # then
        self.assertEqual(test_user.username, 'heisenberg')
        self.assertNotEqual(test_user.hash, 'my-password')
        self.assertEqual(test_user.f_name, 'walter')
        self.assertEqual(test_user.surname, 'white')
        self.assertEqual(test_user.email, 'walter@white.com')
        self.assertEqual(test_user.last_login, date.today())
        self.assertIsInstance(test_user, User)

    def test_create_new_user_with_invalid_email_raises_value_error(self):
        # given
        test_user = None

        # when
        try:
            test_user = User(username='heisenberg', password='my-password', f_name='walter', surname='white',
                             email='invalid_email', last_login=date.today())

        # then
        except InvalidEmailError as error:
            self.assertIsInstance(error, InvalidEmailError)
            self.assertEqual(messages.INVALID_EMAIL_ADDRESS, str(error))
            self.assertIsNone(test_user)
        else:
            self.fail('InvalidEmailError not raised')

    def test_create_new_player_returns_player(self):
        # given
        test_user = create_test_user()

        # when
        test_player = Player(test_user, 'player1')

        # then
        self.assertEqual(test_player.user_id, test_user.id)
        self.assertEqual(test_player.user, test_user)
        self.assertIsInstance(test_player.user, User)
        self.assertEqual(test_player.name, 'player1')
        self.assertIsInstance(test_player, Player)

    def test_create_new_persona_returns_persona(self):
        # given
        test_player = Player(create_test_user(), 'player1')

        # when
        test_persona = Persona(name='Princess', image='princess.jpg', player=test_player)

        # then
        self.assertEqual(test_persona.name, 'Princess')
        self.assertEqual(test_persona.image, 'princess.jpg')
        self.assertEqual(test_persona.player, test_player)
        self.assertIsInstance(test_persona.player, Player)
        self.assertEqual(test_persona.created_by, test_player.id)
        self.assertIsInstance(test_persona, Persona)

    def test_create_new_game_returns_game(self):
        # given
        test_player = Player(create_test_user(), 'player1')
        test_persona = Persona(name='Princess', image='princess.jpg', player=test_player)

        # when
        test_game = Game(player=test_player, persona=test_persona, score=1000, level=10, datetime=date.today())

        # then
        self.assertEqual(test_game.player, test_player)
        self.assertIsInstance(test_game.player, Player)
        self.assertEqual(test_game.persona, test_persona)
        self.assertIsInstance(test_game.persona, Persona)
        self.assertEqual(test_game.score, 1000)
        self.assertEqual(test_game.level, 10)
        self.assertEqual(test_game.datetime, date.today())
        self.assertIsInstance(test_game, Game)


class TestUserMethods(unittest.TestCase):
    """Unit tests for methods of the User class"""
    def test_check_password_with_same_password_returns_true(self):
        # given
        test_user = create_test_user()

        # when
        result = test_user.check_password('my-password')

        # then
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
