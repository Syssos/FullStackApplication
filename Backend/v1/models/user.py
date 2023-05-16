#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Hocus Pocus User Class

The User class is used to define a user of the application.
This class has the key responsability of keeping track of
important user information such as shopping carts, addresses,
contact information, shipping information and the likes. This
class will have many attributes not intended to be publicly
accessed, there for it will have a higher focus aorund security
then "products" on the website.

Below is a list of definitions for each attribute.

Username - The username is a unique string used to publicly identify the specific user.
Password - This value will be stored as a hash, and used to authenticate the user.
Email - This will be used for any automated email services (Primary focus on initial user account creation)
"""

# Standard library imports
from os import getenv

# Related third party imports
from sqlalchemy import Column, String

# Local application/library specific imports
from models.user_base import UserBase, Base

class User(UserBase, Base):
    # For use with SQLalchemy, database table tied to class, can be ingored with current version of backend
    __tablename__ = "users"
    
    if getenv("STORAGE_TYPE") == "db":
        Username = Column(String(60))
        Password = Column(String(160))
        Email = Column(String(160))
    else:
        Username = ""
        Password = ""
        Email = ""