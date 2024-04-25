#!/usr/bin/env python3
"""
0. User model
mandatory
Create a SQLAlchemy model named `User` for a database table
named users (by using the mapping declaration of SQLAlchemy).
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    User model that defines the users table.
    Contains basic user information and authentication information.
    """
    
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

    def __repr__(self):
        """
        representation of the User model
        """
        return f"User: id={self.id}"
