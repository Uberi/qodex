from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()

engine = create_engine("sqlite:///sqlalchemy_example.db")
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine) # create all tables in the engine