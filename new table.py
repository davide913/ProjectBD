import sqlalchemy
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URI = 'postgresql://postgres:davidefinesso9@localhost:5432/BD-2' #inserire pwd giusta
engine = create_engine(DATABASE_URI, echo = True)
Base = declarative_base()                      # tabella = classe che eredita da Base

def my_fun():
    # SQLite supporta database transienti in RAM (echo attiva il logging)

    class Pwd(Base):
        __tablename__ = 'password'                   # obbligatorio

        #extend_existing=True
        
        id_utente = Column(Integer, primary_key=True)    # almeno un attributo deve fare parte della primary key
        name = Column(String)
        password = Column(String)
        



    Pwd.__table__                               #
    Base.metadata.create_all(engine)            #commit della tabella


my_fun()
