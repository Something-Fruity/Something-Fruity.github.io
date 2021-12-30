from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from flaskr.models.base import Base


class Player(Base):
    __tablename__ = 'player'

    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('account.id'))
    name = Column(String)
    account = relationship("Account", backref="player")

    def __init__(self, account, name):
        self.account = account
        self.name = name

