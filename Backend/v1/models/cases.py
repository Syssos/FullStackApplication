#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Hocus Pocus Case Class

The Case class is used to identify any kind of computer
case. These items should usually always be considered
as the platform type "Desktop". Below you can find the
unique attributes of the Case class defined.

Brand - String, The brand that makes the computer case
Model - String, The model of computer case
Size - String, Defining the size of motherboard that fits the case, ie Full, Micro, etc... 
"""

# Standard library imports
from os import getenv

# Related third party imports
from sqlalchemy import Column, String

# Local application/library specific imports
from models.base_model import BaseModel, Base

class Case(BaseModel, Base):
    # For use with SQLalchemy, database table tied to class, can be ingored with current version of backend
    __tablename__ = "cases"
    
    if getenv("STORAGE_TYPE") == "db":
        Brand = Column(String(128), nullable=False)
        Model = Column(String(128))
        Size = Column(String(128))
    else:
        Brand = ""
        Model = ""
        Size = ""