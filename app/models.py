

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

    # Base.metadata.create_all(engine)
    # Session = sessionmaker(bind=engine)
    # session = Session()

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
           return f"{self.name}"\
                + f"{self.email}"\
                + f"{self.phone_number}"
      
      
Base.metadata.create_all(engine)

          #testing user table 

# def test_users(session):
#      mike = User(name="mike",email= "mike@gmail.com", phone_number=709090909)
#      session.add(mike)
#      session.commit()

#      query = session.query(User).filter_by(name="mike").first()

#      if query:
#           print(query.email)
#      else:
#           print("None")

# Session = sessionmaker(bind=engine)
# session = Session()

# test_users(session)








                 # Testing for adding data to book table and query
# def testing_book(session):
#         great_Gatsby = Book(
#             title="The Great Gabsy",
#             author="Matthew",
#             publication_date="1782-09-09",
#             genre="Fiction",
#             availability=True
#         )

#         session.add(great_Gatsby)
#         session.commit()

        
#     # Correct the date format in the filter
#         query = session.query(Book).filter_by(author="Matthew", publication_date="1782-09-09").first()

#         if query:
#           print(f"Book found: {query.title}")
#         else:
#           print("Book not found.")

#     # Close the session
#         session.close()

# # Call the test function with the existing session
# Session = sessionmaker(bind=engine)
# current_session = Session()
# testing_book(current_session)


