"""This module creates a database engine with a session connected to it."""
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


db = create_engine(os.environ.get('DATABASE_URL'))
Session = sessionmaker(bind=db)

Base = declarative_base()
