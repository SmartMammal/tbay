from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    #There is a relationship between Person model and Passport model
    #Passport field here is regular part of person
    # uselist=False arg: passport is a single object rather than list
    # backref="owner" arg: access passport thru person, but also vice versa
    passport = relationship("Passport", uselist=False, backref="owner")

class Passport(Base):
    __tablename__ = 'passport'
    id = Column(Integer, primary_key=True)
    issue_date = Column(Date, nullable=False, default=datetime.utcnow)

    #The integer field owner_id refers to an existing row in the person table
    #How? Using the ForeignKey constraint
    owner_id = Column(Integer, ForeignKey('person.id'), nullable=False)

beyonce = Person(name="Beyonce Knowles") #Creates person
passport = Passport() #Creates empty passport
beyonce.passport = passport #Links the passport to the person's passport

session.add(beyonce) #Adds person to the database
session.commit() #executes command

print beyonce.passport.issue_date
print passport.owner.name