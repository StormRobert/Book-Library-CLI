from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///library.db')

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
        self.publication_date = publication_date
        self.genre = genre
        self.availability = availability
