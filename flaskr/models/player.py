"""Defines a player class mapped to the player table in the  database"""

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from flaskr.models.base import Base


class Player(Base):  # pylint: disable=too-few-public-methods
    """Stores a player details, one account can have many players registered"""
    __tablename__ = 'player'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    name = Column(String)
    user = relationship("User", back_populates="players")
    personas = relationship("Persona", back_populates="player", cascade="all, delete, delete-orphan")
    games = relationship("Game", back_populates="player", cascade="all, delete, delete-orphan")

    def __init__(self, user, name):
        self.user = user
        self.name = name
