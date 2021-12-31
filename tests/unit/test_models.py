import unittest

from flaskr.models.user import User


class TestModels(unittest.TestCase):
    def test_new_user(self):
        """
        GIVEN a User model
        WHEN a new User is created
        THEN check all fields are defined correctly
        """
        user = User('username', 'FlaskIsAwesome')
        assert user.email == 'patkennedy79@gmail.com'
        assert user.hashed_password != 'FlaskIsAwesome'
        assert user.role == 'user'


if __name__ == '__main__':
    unittest.main()
