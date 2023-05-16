#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Hocus Pocus Cable Class

The Cable class is used to identify any kind of "loose"
cable. These can be ethernet cords, HDMI cables, Power
Cables and more. This class has 2 unique identifiers 
explained below.

Type - String, used to define the type of cable, ie VGA, HDMI, etc...
Length - Int, The length of the cable in ft.
"""

# Standard library imports
from os import getenv

# Related third party imports
from sqlalchemy import Column, String, Integer

# Local application/library specific imports
from models.base_model import BaseModel, Base

class Cable(BaseModel, Base):
    # For use with SQLalchemy, database table tied to class, can be ingored with current version of backend
    __tablename__ = "cables"
    
    if getenv("STORAGE_TYPE") == "db":
        Type = Column(String(128), nullable=False)
        Length = Column(Integer())
    else:
        Type = ""
        Length = ""