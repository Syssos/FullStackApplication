#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Hocus Pocus CPU Class

The CPU class is used to identify any kind of CPU.
These items should usually always be considered
as the platform type "Desktop". Below you can find the
unique attributes of the CPU class defined.

Brand - String, The brand that makes the CPU
Model - String, The model of CPU
Speed - Int, Defines the speed of the cpu in Ghz
Cores - Int, Defines the amount of cores the CPU has
"""

# Standard library imports
from os import getenv

# Related third party imports
from sqlalchemy import Column, String, Integer

# Local application/library specific imports
from models.base_model import BaseModel, Base

class CPU(BaseModel, Base):
    # For use with SQLalchemy, database table tied to class, can be ingored with current version of backend
    __tablename__ = "cpus"
    
    if getenv("STORAGE_TYPE") == "db":
        Brand = Column(String(128), nullable=False)
        Model = Column(String(128))
        Speed = Column(Integer())
        Cores = Column(Integer())
        # SocketType = "LGA 1200" Needs to be added
    else:
        Brand = ""
        Model = ""
        Speed = 0
        Cores = 0