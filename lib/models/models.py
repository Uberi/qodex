from sqlalchemy import Column, ForeignKey, Integer, Float, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

import hashlib

Base = declarative_base()

engine = create_engine("sqlite:///database.db")
Session = sessionmaker(bind=engine)

# many-by-many relationship tables
user_group = Table('user_groups', Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('group_id', Integer, ForeignKey('group.id')))

group_books = Table('group_books', Base.metadata,
    Column('group_id', Integer, ForeignKey('group.id')),
    Column('book_id', Integer, ForeignKey('book.id')))

from contextlib import contextmanager

@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    password_hash = Column(String(64), nullable=False)
    email = Column(String(250), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    groups = relationship('Group', secondary=user_group, backref='user')

    def __init__(self, name, password, email, latitude, longitude):
        hashed = hashlib.sha512(bytes(password, "UTF-8")).hexdigest()
        self.name = name
        self.password_hash = hashed
        self.email = email
        self.latitude = latitude
        self.longitude = longitude

    @staticmethod
    def query_by_id(session, id):
        session.query(User).filter_by(id=id).first()

    @staticmethod
    def query_by_email_address(session, email_address):
        session.query(User).filter_by(email_address=email_address).first()

    @staticmethod
    def list(session, filter = ""):
        return session.query(User).all()

    def authenticate(self, password):
        hashed = hashlib.sha512(bytes(password, "UTF-8")).hexdigest()
        return hashed == self.password_hash

    def join_group(self, group):
        self.groups.append(group)
    
    def leave_group(self, group):
        self.groups.remove(group)

class Group(Base):
    __tablename__ = "group"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    books = relationship('Book', secondary=group_books, backref='group')

    def __init__(self, title, password = None):
        hashed = hashlib.sha512(bytes(password, "UTF-8")).hexdigest()
        self.title = title
        self.password_hash = hashed

    @staticmethod
    def list(session, filter = ""):
        return session.query(Group).all()

    def add_book(self, book):
        self.books.append(book)
    
    def remove_book(self, book):
        self.books.remove(book)

class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    isbn = Column(String(250), nullable=False)
    author = Column(String(250), nullable=False)

    def __init__(self, title, isbn, author):
        self.title = title
        self.isbn = isbn
        self.author = author

Base.metadata.create_all(engine) # create all tables in the engine