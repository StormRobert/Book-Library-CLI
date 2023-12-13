from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    full_name = Column(String)
    date_of_birth = Column(DateTime)
    address = Column(String)
    phone_number = Column(String)
    membership_status = Column(String)
    


    # Define the relationship with Book
    books = relationship('Book', back_populates='owner')

