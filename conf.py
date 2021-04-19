import sqlalchemy
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#import psycopg2


DATABASE_URI = 'postgresql://postgres:davidefinesso9@localhost:5432/BD-2' #inserire pwd giusta
engine = create_engine(DATABASE_URI, echo = True)
Base = declarative_base()                      # tabella = classe che eredita da Base

def my_fun():
    # SQLite supporta database transienti in RAM (echo attiva il logging)

    class User(Base):
        __tablename__ = 'users'                   # obbligatorio
        extend_existing=True
        id = Column(Integer, primary_key=True)    # almeno un attributo deve fare parte della primary key
        name = Column(String)
        fullname = Column(String)
        nickname = Column(String)
        
        # questo metodo è opzionale, serve solo per pretty printing
        def __repr__(self):
            return "<User(name='%s', fullname='%s', nickname='%s')>" % (self.name, self.fullname, self.nickname)



    User.__table__                              #
    Base.metadata.create_all(engine)            #commit della tabella
    return Base , engine, User

#test.my_fun()

#myBase = my_fun()

#myBase.metadata.drop_all(engine)         #cancella tutte le tabelle


#ed_user = User(name='franco', fullname='franco furman', nickname='fur')
#print(ed_user.name)
#print(ed_user.nickname)
#print(ed_user.id)

##Session = sessionmaker(bind=engine)       # creazione della factory
##session = Session()

#session.add(ed_user)  # pending instance: verrà salvata nel database quando veramente necessario

#our_user = session.query(User).filter_by(name='franco').first()    # qui è necessario salvare la pending instance
#our_user

#__repr__(User)

#ed_user is our_user

#print(ed_user.id)    # primary key creata in fase di scrittura al database

#ed_user.nickname = 'eddie'

#session.add_all([User(name='wendy', fullname='Wendy Williams', nickname='windy'),
 #                User(name='mary', fullname='Mary Contrary', nickname='mary'),
#                 User(name='fred', fullname='Fred Flintstone', nickname='freddy')])


#print("Dirty instances: " + str(session.dirty))
#print("Pending instances: " + str(session.new) + "\n")
#session.commit()                                            #le istanze vengono "realmente salvate all'interno del DB"
#print("\nDirty instances: " + str(session.dirty))
#print("Pending instances: " + str(session.new))
