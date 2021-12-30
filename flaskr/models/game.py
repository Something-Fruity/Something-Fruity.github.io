from sqlalchemy import Column, Date, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref

from flaskr.models.base import Base


class Game(Base):
    __tablename__ = 'game'

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('player.id'))
    persona_id = Column(Integer, ForeignKey('persona.id'))
    score = Column(Integer)
    level = Column(Integer)
    datetime = Column(Date)
    player = relationship("Player", backref=backref("game", uselist=False))
    persona = relationship("Persona", backref=backref("persona", uselist=False))

    def __init__(self, player, persona, score, level, datetime):
        self.player = player
        self.persona = persona
        self.score = score
        self.level = level
        self.datetime = datetime


