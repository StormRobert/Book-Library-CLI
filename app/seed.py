#!usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import random
from models import Base, Book, User, Book_checkout
from faker import Faker
from datetime import timedelta

if __name__ == '__main__':
    engine = create_engine('sqlite:///library.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Book).delete()
    session.query(User).delete()
    session.query(Book_checkout).delete()

    fake = Faker()

    #BOOKS TABLE DATA
    books = []
    for i in range(10):
        book = Book(
            title = fake.catch_phrase(),
            author = fake.name(),
            publication_date = fake.date_of_birth(),
            genre = fake.word(),
            availability = fake.boolean()
            )
        session.add(book)
        books.append(book)
    session.commit()

    #USERS TABLE DATA
    users = []
    for i in range(10):
        user = User(
            name = fake.name(),
            email = fake.email(),
            phone_number=fake.random_int(min=254700000000, max=254799999999)

        )
        session.add(user)
        users.append(user)

    session.commit()

    # BOOK_CHECKOUTS TABLES
    
    books_checked_out=[]

    for i in range(10):
        random_book = random.choice(books)
        random_user = random.choice(users)
        book_checked_out = Book_checkout(
                book = random_book,
                user = random_user,
                genre = fake.word(),
                checkoutDate=fake.date_time_this_year(),
                returnDate = fake.date_time_this_month() + timedelta(days=fake.random_int(min=7, max=30))
        )
        session.add(book_checked_out)
        books_checked_out.append(book_checked_out)
    session.commit()

    print("Total books in library: ", session.query(Book).count())
    print("First user is:", session.query(User).first())
    session.close()
                
                

   

        

