from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()









class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    full_name = Column(String)
    profile_picture_url = Column(String)
    date_of_birth = Column(DateTime)
    address = Column(String)
    phone_number = Column(String)
    membership_status = Column(String)
    roles_permissions = Column(String)  # or List of Strings
    social_media_profiles = Column(String)  # or JSON type
    last_login_timestamp = Column(DateTime)
    account_status = Column(String, default='Active')  # Default to 'Active'

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    # Define the relationship with Book
    books = relationship('Book', back_populates='owner')