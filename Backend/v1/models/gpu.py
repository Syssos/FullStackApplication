#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Hocus Pocus CPU Class

The GPU class is used to identify any kind of GPU.
These items should usually always be considered
as the platform type "Desktop". Below you can find the
unique attributes of the GPU class defined.

Brand - String, The brand that makes the GPU
Model - String, The model of GPU
"""

# Standard library imports
from os import getenv

# Related third party imports
from sqlalchemy import Column, String, Integer

# Local application/library specific imports
from models.base_model import BaseModel, Base

class GPU(BaseModel, Base):
    # For use with SQLalchemy, database table tied to class, can be ingored with current version of backend
    __tablename__ = "gpus"
    
    if getenv("STORAGE_TYPE") == "db":
        Brand = Column(String(128), nullable=False)
        Model = Column(String(128))
    else:
        Brand = ""
        Model = ""