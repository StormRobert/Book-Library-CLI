from models import Book,datetime

def create_book_table(base, engine):
    base.metadata.create_all(engine)

def add_book(session, book):
    session.add(book)
    session.commit()
    print(f"{book.title} by {book.author} added to db.")

def delete_book(session, book_id):
    book = session.query(Book).filter_by(id=book_id).first()
    if book:
        session.delete(book)
        session.commit()
        print(f"Book with id {book_id} deleted from db.")
    else:
        print(f"Book not found.")

def update_book(session, book_id, new_title, new_author, new_publication_date, new_genre, new_availability):
    book = session.query(Book).filter_by(id=book_id).first()
    if book:
        book.title = new_title
        book.author = new_author
        book.publication_date = datetime.strptime(new_publication_date, "%Y-%m-%d").date()
        book.genre = new_genre
        book.availability = new_availability
        session.commit()
        print(f"Book with id {book_id} updated.")
    else:
        print(f"Book not found")