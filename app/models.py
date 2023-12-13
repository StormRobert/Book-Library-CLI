from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///library.db')

Base = declarative_base()

class Book_checkout(Base):
    __tablename__='bookCheckout'


    id = Column(Integer(), primary_key=True)
    bookID = Column(Integer())
    userID = Column(Integer())
    genre = Column(String())
    checkoutDate = Column(Date())
    returnDate = Column(Date())

     def __init__(self, id, bookID, userID, genre, checkoutDate, returnDate):
        self.bookID = bookID
        self.userID = userID
        self.genre = genre
        self.checkoutDate = checkoutDate
        self.returnDate = returnDate