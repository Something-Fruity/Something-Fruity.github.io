import unittest
from datetime import date

from flaskr.errors.errors import InvalidEmailError
from flaskr.models.user import User
from flaskr.models.player import Player
from flaskr.models.persona import Persona
from flaskr.models.game import Game

from flaskr.labels import messages


def create_test_user():
    return User('heisenberg', 'my-password', 'walter', 'white', 'walter@white.com', date.today())


class TestModels(unittest.TestCase):
    def test_create_new_user_returns_User(self):
        # given
        test_user = None

        # when
        test_user = create_test_user()

        # then
        assert test_user.username == 'heisenberg'
        assert test_user.hash != 'my-password'
        assert test_user.f_name == 'walter'
        assert test_user.surname == 'white'
        assert test_user.email == 'walter@white.com'
        assert test_user.last_login == date.today()
        assert type(test_user) == User

    def test_create_new_user_with_invalid_email_raises_ValueError(self):
        # given
        test_user = None

        # when
        try:
            test_user = User(username='heisenberg', password='my-password', f_name='walter', surname='white',
                             email='invalid_email', last_login=date.today())

        # then
        except InvalidEmailError as e:
            self.assertEqual(type(e), InvalidEmailError)
            self.assertEqual(messages.INVALID_EMAIL_ADDRESS, str(e))
            assert test_user is None
        else:
            self.fail('InvalidEmailError not raised')

    def test_create_new_player_returns_Player(self):
        # given
        test_user = create_test_user()

        # when
        test_player = Player(test_user, 'player1')

        # then
        assert test_player.user_id == test_user.id
        assert test_player.user == test_user
        assert type(test_player.user) == User
        assert test_player.name == 'player1'
        assert type(test_player) == Player

    def test_create_new_persona_returns_Persona(self):
        # given
        test_player = Player(create_test_user(), 'player1')

        # when
        test_persona = Persona(name='Princess', image='princess.jpg', player=test_player)

        # then
        assert test_persona.name == 'Princess'
        assert test_persona.image == 'princess.jpg'
        assert test_persona.player == test_player
        assert type(test_persona.player) == Player
        assert test_persona.created_by == test_player.id
        assert type(test_persona) == Persona

    def test_create_new_game_returns_Game(self):
        # given
        test_player = Player(create_test_user(), 'player1')
        test_persona = Persona(name='Princess', image='princess.jpg', player=test_player)

        # when
        test_game = Game(player=test_player, persona=test_persona, score=1000, level=10, datetime=date.today())

        # then
        assert test_game.player == test_player
        assert type(test_game.player) == Player
        assert test_game.persona == test_persona
        assert type(test_game.persona) == Persona
        assert test_game.score == 1000
        assert test_game.level == 10
        assert test_game.datetime == date.today()
        assert type(test_game) == Game


class TestUserMethods(unittest.TestCase):
    def test_check_password_with_same_password_returns_True(self):
        # given
        test_user = create_test_user()

        # when
        result = test_user.check_password('my-password')

        # then
        assert result is True


if __name__ == '__main__':
    unittest.main()
