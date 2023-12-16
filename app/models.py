from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
from prettytable import PrettyTable


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

    def __init__(self, title, author, publication_date, genre, availability=None):
        self.title = title
        self.author = author
        self.publication_date = datetime.strptime(publication_date, "%Y-%m-%d").date()
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

    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number

    def __repr__(self):
        return repr({"id": self.id, "name": self.name, "email": self.email, "phone_number": self.phone_number})

class Book_checkout(Base):
    __tablename__='bookCheckout'

    id = Column(Integer(), primary_key=True)
    bookID = Column(Integer())
    userID = Column(Integer())
    genre = Column(String())
    checkoutDate = Column(Date())
    returnDate = Column(Date())

    def __init__(self, bookID, userID, genre, checkoutDate, returnDate):
        self.bookID = bookID
        self.userID = userID
        self.genre = genre
        self.checkoutDate = checkoutDate
        self.returnDate = returnDate

    def __repr__(self):
        return repr({"id": self.id, "bookID": self.bookID, "userID": self.userID, "genre": self.genre, "checkoutDate": self.checkoutDate, "returnDate": self.returnDate})

Base.metadata.create_all(engine)

def showall(data, table_name):
    """Display all elements in the given data."""
    if not data:
        print(f"No records found in {table_name}")
        return

    table = PrettyTable()
    table.field_names = data[0].__dict__.keys()

    for item in data:
        table.add_row(item.__dict__.values())

    print(f"{table_name.capitalize()}:\n{table}")

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Insert data into the 'books' table for testing
great_Gatsby = Book(
    title="The Great Gatsby",
    author="F. Scott Fitzgerald",
    publication_date="1925-04-10",
    genre="Fiction",
)

session.add(great_Gatsby)
session.commit()

# Query and display the contents of the 'books' table
books = session.query(Book).all()
showall(books, 'books')

# Insert data into the 'users' table for testing
new_user = User(
    name="John Doe",
    email="john.doe@example.com",
    phone_number=1234567890
)

session.add(new_user)
session.commit()

# Query and display the contents of the 'users' table
users = session.query(User).all()
showall(users, 'users')

# Insert data into the 'bookCheckout' table for testing
checkout_entry = Book_checkout(
    bookID=1,  # Assuming bookID corresponds to the ID of 'The Great Gatsby'
    userID=1,  # Assuming userID corresponds to the ID of 'John Doe'
    genre="Fiction",
    checkoutDate=datetime.now(),
    returnDate=datetime.now()
)

session.add(checkout_entry)
session.commit()

# Query and display the contents of the 'bookCheckout' table
book_checkouts = session.query(Book_checkout).all()
showall(book_checkouts, 'bookCheckouts')

# Close the session
session.close()
