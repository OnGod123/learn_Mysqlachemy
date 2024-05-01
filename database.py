from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base class for all our ORM classes
Base = declarative_base()

# Define a class representing your table
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Create a database engine
engine = create_engine('sqlite:///example.db')

# Create the tables in the database
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Create an instance of the User class
new_user = User(name='John', age=30)

# Add the instance to the session
session.add(new_user)

# Commit the session to persist the changes
session.commit()

