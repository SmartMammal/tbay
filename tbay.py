from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#    Q. What about association tables?
#    Q. When to have uselist=False

# In the terminal
# a. "run parts install postgresql"
# b. start the database server by running "parts start postgresql"
# c. then create the db with "createdb tbay"... tbay is the name of the db
# d. dropdb tbay && createdb tbay... this deletes the database and recreates it

# Create Engine - talk to db suing raw SQL
engine = create_engine('postgresql://action:action@localhost:5432/tbay')

# Create Session - cursor queue and execute db transactions.
Session = sessionmaker(bind=engine)
session = Session()

# Declarative base - repository for the models, will issue create table statements
Base = declarative_base()

# Model
from datetime import datetime # Time functions
from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey # datatypes
from sqlalchemy.orm import relationship

class Item(Base): # model represented by class called Item, subclassing base
    __tablename__ = "items" # Used to name the items table in db

    id = Column(Integer, primary_key=True) # An integer primary key
    name = Column(String, nullable=False) # String w/ not null constraint
    description = Column(String) # Decription of the item
    start_time = Column(DateTime, default=datetime.utcnow) # Auction start time defaulted to current UTC time
#    owner_id = Column(Integer, ForeignKey('users.id'), nullable=False)
#    Q. Should owner_id have uselist=false?
#    bids = relationship('Bid', backref='item')

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    
#    item = relationship('Item', backref='owner')
#    bidder = relationship('Bid', backref='bidder')   

class Bid(Base):
    __tablename__ = "bids"
    
    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)
    
#    bidder_id = Column(Integer, ForeignKey('users.id'), nullable=False)
#    Q. Should bidder_id have uselist=false?
#    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
#    Q. Should item_id have uselist=false?


#    Q. What about association tables?
# Create the table
Base.metadata.create_all(engine)

"""
CREATING A USER
"""
# Example: Create a user
#beyonce = User()
#beyonce.username = "bknowles"
#beyonce.password = "crazyinlove"
#session.add(beyonce)
#session.commit()

# Example: Create a user... default __init__ method for models in SQLAlchemy
#beyonce = User(username="bknowles", password="crazyinlove")

"""
QUERYING: Session.query method
"""

# Returns a list of all of the user objects
#session.query(User).all() # Returns a list of all of the user objects

# Returns the first user
#session.query(User).first()

# Finds the user with the primary key equal to 1
#session.query(User).get(1)

# Returns a list of all of the usernames in ascending order
#session.query(User.username).order_by(User.username).all()

# Returns the description of all of the basesballs
#session.query(Item.description).filter(Item.name == "baseball").all()

# Return the item id and description for all baseballs which were created in the past.  Remember to import the datetime object: from datetime import datetime
#session.query(Item.id, Item.description).filter(Item.name == "baseball", Item.start_time < datetime.utcnow()).all()

"""
UPDATING ROWS
"""
#user = session.query(User).first() #find the record
#user.username = "solange" #do update, override existing value
#session.commit() #execute command

"""
DELETING ROWS: session.delete
"""
#user = session.query(User).first() #find the record
#session.delete(user) #do delete
#session.commit() #execute command

"""
NOTE: RELATIONSHIPS
A. 1-to-1: single row of a table to single row of another table... one passport per person AND one person per passport
B. 1-to-many: single row of a table to multiple rows of another... 1 manufacturer per guitar, but several guitars per manufacturer
C. many-to-many: multiple rows of a table to multiple rows of another... pizza with multiple toppings and single topping on multiple pizzas.
"""

