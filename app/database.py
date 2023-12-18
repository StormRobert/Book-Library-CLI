from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Book, User, Book_checkout
from datetime import datetime

database_url='sqlite:///library.db'
engine = create_engine(database_url, echo=False)
Session = sessionmaker(bind=engine)
session = Session()

# -----------------------------Methods for the book table
def get_all_books(session):
    return session.query(Book).all()

def add_book(session, title, author, publication_date, genre, availability=True):
    new_book = Book(title=title, author=author, publication_date=publication_date, genre=genre, availability=availability)
    session.add(new_book)
    session.commit()

def update_book(session, book_id, title=None, author=None, publication_date=None, genre=None, availability=None):
    book = session.query(Book).get(book_id)
    if book:
        if title:
            book.title = title
        if author:
            book.author = author
        if publication_date:
            book.publication_date = publication_date
        if genre:
            book.genre = genre
        if availability is not None:
            book.availability = availability
        session.commit()
        return (f"Book with ID {book_id}updated.")
    else:
        print(f"Book with ID {book_id} not found.")

def delete_book(session, book_id):
    book = session.query(Book).get(book_id)
    if book:
        session.delete(book)
        session.commit()
        return f"{book.title} is being deleted from the database, check the table again for confirmation"
    else:
        print(f"Book with ID {book_id} not found.")


def update_book(session, book_id, new_title, new_author, new_publication_date, new_genre, new_availability):
    book = session.query(Book).filter_by(id=book_id).first()
    if book:
        book.title = new_title
        book.author = new_author
        book.publication_date = new_publication_date
        book.genre = new_genre
        book.availability = new_availability
        session.commit()
        return (f"Book with id {book_id} updated.")
    

# ------------------------Methods for the user table
def get_all_users(session):
    return session.query(User).all()

def add_user(session, name, email, phone_number):
    new_user = User(name=name, email=email, phone_number=phone_number)
    session.add(new_user)
    session.commit()

def delete_user(session, user_id):
    user = session.query(User).get(user_id)
    if user:
        session.delete(user)
        session.commit()
    else:
        print(f"User with ID {user_id} not found.")

#------------------ Methods for the Book_checkout table
def get_all_checkouts(session):
    return session.query(Book_checkout).all()

def checkout_book(session, book_id, user_id, genre, checkout_date=datetime.now(), return_date=datetime ):
    book = session.query(Book).get(book_id)
    user = session.query(User).get(user_id)
    if book and user:
        new_checkout = Book_checkout(book=book, user=user, genre=genre, checkoutDate=checkout_date, returnDate=return_date )
        session.add(new_checkout)
        session.commit()
    else:
        print(f"Book with ID {book_id} or User with ID {user_id} not found.")

def return_book(session, checkout_id, return_date=datetime.now()):
    checkout = session.query(Book_checkout).get(checkout_id)
    if checkout:
        checkout.returnDate = return_date
        session.delete(checkout)
        session.commit()
    else:
        print(f"Checkout with ID {checkout_id} not found.")

# Other methods
def recommend_books(session, user_id):
    user_checkouts = session.query(Book_checkout).filter_by(userID=user_id).all()

    if not user_checkouts:
        print("No past checkouts found for this user.")
        return


    # Count the occurrences of each genre in the user's checkouts
    genre_counts = {}
    for checkout in user_checkouts:
        genre = checkout.genre
        genre_counts[genre] = genre_counts.get(genre, 0) + 1

    # Find the most frequently checked-out genre
    most_frequent_genre = max(genre_counts, key=genre_counts.get)
    print(f"Recommended books for user {user_id} based on past checkouts in the genre '{most_frequent_genre}':")
    
    # Recommend books of the most frequent genre
    return session.query(Book).filter_by(genre=most_frequent_genre).all()

