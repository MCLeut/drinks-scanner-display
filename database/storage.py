from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from env import is_pi

engine = create_engine('postgresql://postgres:postgres@127.0.0.1/drinks', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

if not is_pi():
    import logging
    logger = logging.getLogger('sqlalchemy.engine')
    logger.setLevel(logging.INFO)

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import models
    Base.metadata.create_all(bind=engine)

def get_session():
    db_session.rollback()
    return db_session