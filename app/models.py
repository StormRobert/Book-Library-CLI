from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    email = Column(String(), nullable=False, unique=True)
    full_name = Column(String())
    date_of_birth = Column(DateTime)
    address = Column(String())
    phone_number = Column(String())

    def __init__(self, email, full_name, date_of_birth, address, phone_number):
        self.email = email
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.address = address
        self.phone_number = phone_number

