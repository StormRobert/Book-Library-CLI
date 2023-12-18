from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


engine = create_engine('sqlite:///library.db', echo=False)
Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer(), primary_key=True)
    title = Column(String)
    author = Column(String())
    publication_date = Column(Date())
    genre = Column(String())
    availability = Column(Boolean(), default=True)

    checkouts = relationship('Book_checkout', back_populates='book')

    def __init__(self, title, author, publication_date, genre, availability=None):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.genre = genre
        self.availability = availability

    def __repr__(self):
        return repr({"id": self.id, "title": self.title, "author": self.author, "publication_date": self.publication_date, "genre": self.genre, "availability": self.availability})

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    email = Column(String())
    phone_number = Column(Integer())

    checkouts = relationship('Book_checkout', back_populates='user')

    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        

    def __repr__(self):
        return repr({"id": self.id, "name": self.name, "email": self.email, "phone_number": self.phone_number})

class Book_checkout(Base):
    __tablename__='bookCheckouts'

    id = Column(Integer(), primary_key=True)
    bookID = Column(Integer(), ForeignKey('books.id'))
    userID = Column(Integer(), ForeignKey('users.id') )
    genre = Column(String())
    checkoutDate = Column(Date())
    returnDate = Column(Date())

    book = relationship('Book', back_populates='checkouts')
    user = relationship('User', back_populates='checkouts') 

    def __init__(self,book,user, genre, checkoutDate, returnDate):
        self.book = book
        self.user = user
        self.genre = genre
        self.checkoutDate = checkoutDate
        self.returnDate = returnDate

    def __repr__(self):
        return repr({"id": self.id,"Book":self.book,  "genre": self.genre, "checkoutDate": self.checkoutDate, "returnDate": self.returnDate})
