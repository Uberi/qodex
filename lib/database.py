from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()
 
class User(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    password_hash = Column(String(64), nullable=False)
 
class Address(Base):
    __tablename__ = "address"
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey("person.id"))
    person = relationship(User)

engine = create_engine("sqlite:///sqlalchemy_example.db")
Base.metadata.create_all(engine) # create all tables in the engine