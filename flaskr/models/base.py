"""This module creates a database engine with a session connected to it."""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


db = create_engine('mysql://root:root@mysql-db/sth_fruity')
Session = sessionmaker(bind=db)

Base = declarative_base()
