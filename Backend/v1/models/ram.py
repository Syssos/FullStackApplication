#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Hocus Pocus RAM Class

The GPU class is used to identify any kind of RAM.
This item can be used in either Desktop or Laptops.
Ensure the platform aligns with the type of ram to
prevent confusion in listing location. Below you 
can find the unique attributes of the RAM class defined.

Brand - String, The brand that makes the RAM
Capacity - Int, The totatl capacity of the ram in GB
Speed - Int, The speed of the ram in Mhz
"""

# Standard library imports
from os import getenv

# Related third party imports
from sqlalchemy import Column, String, Integer

# Local application/library specific imports
from models.base_model import BaseModel, Base

class Ram(BaseModel, Base):
    # For use with SQLalchemy, database table tied to class, can be ingored with current version of backend
    __tablename__ = "memory"
    
    if getenv("STORAGE_TYPE") == "db":
        Brand = Column(String(128), nullable=False)
        Model = Column(String(128))
        Capacity = Column(Integer())
        Speed = Column(Integer())
        # SOCKET, ie DDR4, DDR3
        # MAXRAMSPEED, ie 3666, 4200
        # MINRAMSPEED, ie 2400, 2666
    else:
        Brand = ""
        Model = ""
        Capacity = ""
        Speed = ""