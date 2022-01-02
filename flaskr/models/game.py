"""Defines a game class mapped to the game table in the database"""

from sqlalchemy import Column, Date, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref

from flaskr.models.base import Base
# pylint: disable=unused-import
# Disable import linting as these classes are imported to back-fill the relationships
from flaskr.models.player import Player
from flaskr.models.persona import Persona


class Game(Base):  # pylint: disable=too-few-public-methods
    """Stores the game details: player, persona, score, level and date played"""
    __tablename__ = 'game'

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('player.id'))
    persona_id = Column(Integer, ForeignKey('persona.id'))
    score = Column(Integer)
    level = Column(Integer)
    datetime = Column(Date)
    player = relationship("Player", backref=backref("game", uselist=False))
    persona = relationship("Persona", backref=backref("persona", uselist=False))

    # pylint: disable=too-many-arguments
    def __init__(self, player, persona, score, level, datetime):
        self.player = player
        self.persona = persona
        self.score = score
        self.level = level
        self.datetime = datetime
