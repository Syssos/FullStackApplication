#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Hocus Pocus SSD Class

The SSD class is used to identify any kind of SSD.
This item can be used in either Desktop or Laptops.
Ensure the platform aligns with the type of ram to
prevent confusion in listing location. Below you 
can find the unique attributes of the SSD class defined.

Brand - String, The brand that makes the SSD
Connection - String, The connection type, ie "SATA", "M.2", etc...
Capacity - Int, The size of the Solid State Drive in GB
"""

# Standard library imports
from os import getenv

# Related third party imports
from sqlalchemy import Column, String, Integer

# Local application/library specific imports
from models.base_model import BaseModel, Base

class SSD(BaseModel, Base):
    # For use with SQLalchemy, database table tied to class
    __tablename__ = "ssds"
    
    if getenv("STORAGE_TYPE") == "db":
        Brand = Column(String(128), nullable=False)
        Connection= Column(String(128))
        Capacity = Column(Integer())
    else:
        Brand = ""
        Connection = ""
        Capacity = 0
