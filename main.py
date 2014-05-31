import os, sys
import random
import string
import hashlib

import cherrypy
import lib.MakoTool
cherrypy.tools.render = MakoTool()

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

class Qodex(object):
    @cherrypy.expose
    @cherrypy.tools.user()
    
    def index(self):
        pass

    @cherrypy.expose
    def logout(self):
        cherrypy.lib.sessions.expire()

    @cherrypy.expose
    def generate(self, length=8):
        some_string = "".join(random.sample(string.hexdigits, int(length)))
        cherrypy.session["mystring"] = some_string
        return some_string

    @cherrypy.expose
    def display(self):
        return cherrypy.session["mystring"]

if __name__ == "__main__":
    configuration = {
        "/": {
            "tools.sessions.on": True,
            "tools.staticdir.root": os.path.abspath(os.getcwd()),

            "server.socket_host": "0.0.0.0",
            "server.socket_port": 443,

            "server.ssl_module": "builtin",
            "server.ssl_certificate": "./ssl/certificate.crt",
            "server.ssl_private_key": "./ssl/private_key.key",
            "server.ssl_certificate_chain": "./ssl/certificate_chain.crt",
        },
        "/static": {
            "tools.staticdir.on": True,
            "tools.staticdir.dir": "./static",
        }
    }
    cherrypy.quickstart(Qodex(), "/", configuration)
