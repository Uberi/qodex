from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

if (not Base):
    Base = declarative_base()

    engine = create_engine("sqlite:///sqlalchemy_example.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine) # create all tables in the engine

# many-by-many relationship tables
user_group = Table('user_groups', Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('group_id', Integer, ForeignKey('group.id')))

group_books = Table('group_books', Base.metadata,
    Column('group_id', Integer, ForeignKey('group.id')),
    Column('book_id', Integer, ForeignKey('book.id')))


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    password = Column(String(64), nullable=False)
    email_address = Column(String(250), nullable=False)
    groups = relationship('Group', secondary=user_group, backref='user')

    def __init__(self, name, password, email_address):
        this.name = name
        this.password = password
        this.email_address = email_address

    # query_by_id: returns the User instance with the given id.
    @staticmethod
    def query_by_id(id):
        session.query(User).filter_by(id=id).first()

    @staticmethod
    def query_by_email_address(email_address):
        session.query(User).filter_by(email_address=email_address).first()

    def authenticate(self, password):
        return (password == self.password)

class Group(Base):
    __tablename__ = "group"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    books = relationship('Book', secondary=group_books, backref='group')

    def __init__(self, d, password, email_address):
        this.name = name
        this.password = password
        this.email_address = email_address

    def add_user(user_id):
        return


class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)

    def __init__(self, name, password, email_address):
        this.name = name
        this.password = password
        this.email_address = email_address


'''
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
'''




