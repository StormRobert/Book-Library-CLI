from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import datetime


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

this is my code in the models.py file . ths is the foundation of the book library CLI app I will be creating using python. 

the database.py file will define all methods related to data manipulation for the database. The methods include
 --methods for the book table--
get_all_books() - gets information on all books
add_book()
update_book()
delete_book()

--methods for the user table--
get _all_users() - gets information on all users
add_user()
delete_user()

--methods for the Book_checkout table --
get_all_checkouts()
checkout_book()
return_book()

otherMethods
reccomend_books() recomends books to user based on the genre of past book checkouts in the BookCheckout table

the bookLibrary.py file is the application itself. all methods in the database .py will be called here as app commands . the app commands defined will be used as commands when interacting with the application itself.
such commands include
show _library() - calls the methods get_all_books() ,  get _all_users()  ,  get_all_checkouts() and displays the data in their respective tables.

add_book()
update_book()
delete_book()
add_user()
delete_user()
checkout_book()
return_book()
reccomend_books() - this methods will be app commands that will call the methods with the exact same name.