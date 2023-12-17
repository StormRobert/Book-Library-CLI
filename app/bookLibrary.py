#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from models import Base, Book,User,Book_checkout
from database import add_book, update_book, delete_book, get_all_Books, add_user, delete_user

import typer
from rich.console import Console
from rich.table import Table

console = Console()

app = typer.Typer()


if __name__ == "__main__":
    engine = create_engine('sqlite:///library.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

@app.command()
def showBooks():
    books = get_all_books()

    # #BOOK TABLE METHODS
    #             # ADDING A BOOK TO THE TABLE
    # Vampire_diaries = Book(title="Vampire Diaries", author="MAtthew ",publication_date=datetime.strptime("1997-10-22", "%Y-%m-%d").date(), genre="Fiction", availability=1)
    # print(f" {add_book(session, Vampire_diaries)} ")
    #             #UPDATING A BOOK THAT IS ALREADY IN THE DATABASE
    # existing_book = session.query(Book).filter_by(title="Vampire Diaries").first()
    # if existing_book:
    #     existing_book.title = "Vampires"
    #     existing_book.author = "ELIJAH"
    #     existing_book.publication_date = datetime.strptime("1997-10-22", "%Y-%m-%d").date()
    #     existing_book.genre = "Adventure"
    #     existing_book.availability = 1
    #     session.commit()
    #     print(f"{update_book(session, existing_book.id, 'Vampires', 'ELIJAH', datetime.strptime('1997-10-22', '%Y-%m-%d').date(), 'Adventure', 1)}")
    # else:
    #     print("Book not found")

    #             #DELETING AN EXISTING BOOK
    # book = session.query(Book).filter_by(title="Streamlined holistic function").first()
    # if book:
    #     print(f"{delete_book(session, book)}")
    # else:
    #     print("Book non-existent because it's deleted")


    #             #ADDING A NEW USER TO THE USERS TABLE
    # Messi = User(name="Messi", email="messi@gmail.com", phone_number=254722806547)
    # print(f"{add_user(session,Messi)}")
    #             #DELETING AN EXISTING USER FROM THE USERS TABLE
    # Jacob = session.query(User).filter_by(name = "Jacob Little").first()
    # print({delete_user(session, Jacob)})

