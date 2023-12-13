from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
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
    availability = Column(Boolean())

    def __init__(self, title, author, publication_date, genre, availability=True):
        self.title = title
        self.author = author
        self.publication_date = datetime.strptime(publication_date, "%Y-%m-%d").date()
        self.genre = genre
        self.availability = availability

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

class BookLibrary:
    def add_book(self, book):
        session.add(book)
        session.commit()

    def delete_book(self, book_id):
        book = session.query(Book).get(book_id)
        if book:
            session.delete(book)
            session.commit()

    def update_book(self, book_id, new_title=None, new_author=None, new_publication_date=None, new_genre=None, new_availability=None):
        book = session.query(Book).get(book_id)
        if book:
            if new_title is not None:
                book.title = new_title
            if new_author is not None:
                book.author = new_author
            if new_publication_date is not None:
                book.publication_date = datetime.strptime(new_publication_date, "%Y-%m-%d").date()
            if new_genre is not None:
                book.genre = new_genre
            if new_availability is not None:
                book.availability = new_availability

            session.commit()

library = BookLibrary()

# Adding books
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "1925-04-10", "Fiction")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "1960-07-11", "Fiction")
library.add_book(book1)
library.add_book(book2)

# Updating a book
library.update_book(1, new_title="The Great Gatsby (Updated)", new_author="F. S. Fitzgerald (Updated)")

# Deleting a book
library.delete_book(2)

# Print the updated library
books = session.query(Book).all()
for book in books:
    print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Publication Date: {book.publication_date}, Genre: {book.genre}, Availability: {book.availability}")           