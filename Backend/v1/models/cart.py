#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Hocus Pocus Cart Class

The Cart class is a considered a "private" class of the
application. This means it is not intended to be publicly
accessable like "product" class instances.
"""

# Standard library imports
from os import getenv

# Related third party imports
from sqlalchemy import Column, String

# Local application/library specific imports
from models.user_base import UserBase, Base

class Cart(UserBase, Base):
    # For use with SQLalchemy, database table tied to class, can be ingored with current version of backend
    __tablename__ = "carts"
    
    if getenv("STORAGE_TYPE") == "db":
        User = Column(String(60))
        # items = [sku#, sku#, sku#]
        # many to many relationship with items?
    else:
        User = ""
        Items = []