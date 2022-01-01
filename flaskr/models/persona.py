"""Defines a persona class mapped to the persona table in the database"""

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from flaskr.models.base import Base


class Persona(Base):  # pylint: disable=too-few-public-methods
    """Stores the personas a player can use when playing a game"""
    __tablename__ = 'persona'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    image = Column(String)
    created_by = Column(Integer, ForeignKey('player.id'))
    player = relationship("Player", backref="persona")

    def ___init__(self, name, image, player):
        self.name = name
        self.image = image
        self.player = player
