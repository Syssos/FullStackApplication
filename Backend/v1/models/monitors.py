#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Hocus Pocus Monitor Class

The Monitor class is used to identify any kind of 
Monitor. These items should usually always be 
considered as the platform type "Desktop". Below 
you can find the unique attributes of the Monitor
class defined.

Brand - String, The brand that makes the monitor
Model - String, The model of monitor
Size - Int, The size of the monitor in inches
"""

# Standard library imports
from os import getenv

# Related third party imports
from sqlalchemy import Column, String, Integer

# Local application/library specific imports
from models.base_model import BaseModel, Base

class Monitor(BaseModel, Base):
    # For use with SQLalchemy, database table tied to class, can be ingored with current version of backend
    __tablename__ = "monitor"
    
    if getenv("STORAGE_TYPE") == "db":
        Brand = Column(String(128), nullable=False)
        Ports = Column(String(128))
        Size = Column(Integer())
    else:
        Brand = ""
        Ports = ""
        Size = 0