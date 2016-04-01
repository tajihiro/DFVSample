from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import db_uri

engine = create_engine(db_uri, convert_unicode=True, encoding='utf-8', echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=True,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

# def init_db():
#     import models
#     Base.metadata.create_all(bind=engine)