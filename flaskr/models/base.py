from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = create_engine('mysql://root:root@127.0.0.1/sth_fruity')
Session = sessionmaker(bind=db)

Base = declarative_base()
