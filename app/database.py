from models import Book, User, Book_checkout , sessionmaker, create_engine, Base

engine = create_engine('sqlite:///library.db')
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)
def add_book(session, book):
    existing_book = session.query(Book).filter_by(title=book.title).first()
    if existing_book:
        return "Book already exists"
    else:

      session.add(book)
    session.commit()
    return f"Book {book.title} added successfully."
    

def delete_book(session, book):
        session.delete(book)
        session.commit()
        return f"{book.title} is being deleted from the database, check the table again for confirmation"
        

def update_book(session, book_id, new_title, new_author, new_publication_date, new_genre, new_availability):
    book = session.query(Book).filter_by(id=book_id).first()
    if book:
        book.title = new_title
        book.author = new_author
        book.publication_date = new_publication_date
        book.genre = new_genre
        book.availability = new_availability
        session.commit()
        return (f"Book with id {book_id}updated.")
    
def add_user(session, user):
    existing_user = session.query(User).filter_by(name = user.name).first()
    if existing_user:
        return f"{user.name} exists"
    else:
       session.add(user)
       session.commit()  
       return f"{user.name} added to the users table"  
    
def delete_user(session,user):
    if user:
        existing_user = session.query(User).filter_by(name = user.name).first()
        if existing_user:
            session.delete(user)
            session.commit()
            return f"{user.name} is being deleted from the database , check table to confirm"
        else:
            return f"{user.name} has been deleted from the database"
    else:
        return f"delete successfull"
