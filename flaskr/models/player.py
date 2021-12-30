from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from flaskr.models.base import Base


class Player(Base):
    __tablename__ = 'player'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    name = Column(String)
    user = relationship("User", backref="player")

    def __init__(self, user, name):
        self.user = user
        self.name = name

