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
        """
        GIVEN a User model
        WHEN a new User is created
        THEN check all fields are defined correctly and the password is not stored as a raw string
        """
        test_user = create_test_user()
        assert test_user.username == 'heisenberg'
        assert test_user.hash != 'my-password'
        assert test_user.f_name == 'walter'
        assert test_user.surname == 'white'
        assert test_user.email == 'walter@white.com'
        assert test_user.last_login == date.today()
        assert type(test_user) == User

    def test_create_new_user_with_invalid_email_raises_ValueError(self):
        """
        GIVEN a User model
        WHEN a new User is created with an invalid email address
        THEN an InvalidEmailError is raised and the user is not created
        """
        try:
            test_user = None
            test_user = User(username='heisenberg', password='my-password', f_name='walter', surname='white',
                             email='invalid_email', last_login=date.today())
        except InvalidEmailError as e:
            self.assertEqual(type(e), InvalidEmailError)
            self.assertEqual(messages.INVALID_EMAIL_ADDRESS, str(e))
            assert test_user is None
        else:
            self.fail('InvalidEmailError not raised')

    def test_create_new_player_returns_Player(self):
        """
        GIVEN a Player model
        WHEN a new Player is created
        THEN check all fields are defined correctly
        """
        test_user = create_test_user()
        test_player = Player(test_user, 'player1')

        assert test_player.user_id == test_user.id
        assert test_player.user == test_user
        assert type(test_player.user) == User
        assert test_player.name == 'player1'
        assert type(test_player) == Player

    def test_create_new_persona_returns_Persona(self):
        """
        GIVEN a Persona model
        WHEN a new Persona is created
        THEN check all fields are defined correctly
        """
        test_player = Player(create_test_user(), 'player1')
        persona = Persona(name='Princess', image='princess.jpg', player=test_player)

        assert persona.name == 'Princess'
        assert persona.image == 'princess.jpg'
        assert persona.player == test_player
        assert type(persona.player) == Player
        assert persona.created_by == test_player.id
        assert type(persona) == Persona

    def test_create_new_game_returns_Game(self):
        """
        GIVEN a Game model
        WHEN a new Game is created
        THEN check all fields are defined correctly
        """
        test_player = Player(create_test_user(), 'player1')
        test_persona = Persona(name='Princess', image='princess.jpg', player=test_player)
        test_game = Game(player=test_player, persona=test_persona, score=1000, level=10, datetime=date.today())

        assert test_game.player == test_player
        assert type(test_game.player) == Player
        assert test_game.persona == test_persona
        assert type(test_game.persona) == Persona
        assert test_game.score == 1000
        assert test_game.level == 10
        assert test_game.datetime == date.today()
        assert type(test_game) == Game


if __name__ == '__main__':
    unittest.main()
