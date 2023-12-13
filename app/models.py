

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


