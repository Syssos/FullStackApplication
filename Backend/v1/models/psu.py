#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Hocus Pocus PSU Class

The GPU class is used to identify any kind of PSU.
These items should usually always be considered
as the platform type "Desktop". Below you can find the
unique attributes of the PSU class defined.

Brand - String, The brand that makes the PSU
PowerAmount - Int, The amouint of power the powersupply is capable of making
"""

# Standard library imports
from os import getenv

# Related third party imports
from sqlalchemy import Column, String, Integer

# Local application/library specific imports
from models.base_model import BaseModel, Base

class PSU(BaseModel, Base):
    # For use with SQLalchemy, database table tied to class, can be ingored with current version of backend
    __tablename__ = "psus"
    
    if getenv("STORAGE_TYPE") == "db":
        Brand = Column(String(128), nullable=False)
        PowerAmount = Column(Integer())
    else:
        Brand = ""
        PowerAmount = 0