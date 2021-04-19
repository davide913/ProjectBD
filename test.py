import sqlalchemy
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import conf

Base, engine, User= conf.my_fun()

Session = sessionmaker(bind=engine)       # creazione della factory
session = Session()


session.add_all([User(name='wendy', fullname='Wendy Williams', nickname='windy'),
                 User(name='mary', fullname='Mary Contrary', nickname='mary'),
                 User(name='fred', fullname='Fred Flintstone', nickname='freddy')])


print("Dirty instances: " + str(session.dirty))
print("Pending instances: " + str(session.new) + "\n")
session.commit()                                            #le istanze vengono "realmente salvate all'interno del DB"
print("\nDirty instances: " + str(session.dirty))
print("Pending instances: " + str(session.new))
