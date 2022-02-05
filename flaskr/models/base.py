"""This module creates a database engine with a session connected to it."""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#below commented out by Lukasz, do not remove it please
#db = create_engine('mysql://root:root@172.19.0.2/sth_fruity')
#db = create_engine('mysql://root:root@127.0.0.0/sth_fruity')

db = create_engine('mysql://root:root@mysql-db/sth_fruity')
Session = sessionmaker(bind=db)

Base = declarative_base()
