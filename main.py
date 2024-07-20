from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an engine
engine = create_engine('sqlite:///example.db', echo=True)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a Session
session = Session()

# Declare a Base for our classes
Base = declarative_base()

# Define a sample table as a Python class
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Create all tables
Base.metadata.create_all(engine)

# Add a new record
new_user = User(name='John Doe', age=30)
session.add(new_user)
session.commit()

# Query the database
for user in session.query(User).all():
    print(user.name, user.age)
