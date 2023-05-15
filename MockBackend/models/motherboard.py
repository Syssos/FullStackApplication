#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Hocus Pocus Motherboard Class

The Monitor class is used to identify any kind of 
Motherboard. These items should usually always be 
considered as the platform type "Desktop". Below 
you can find the unique attributes of the 
Motherboard class defined.

Brand - String, The brand that makes the monitor
Model - String, The model of monitor
VideoOut - String, 
Socket - String,
RAMType - String, The RAM socket type of the motherboard, ie DDR4
RAMSlots - Int, The amount of ram slots on the motherboard
MAXRAMSPEED - Int, the max ram speed alotted by the motherboard
MINRAMSPEED - Int, the minimum ram speed of the motherboard
NVMeSLOTS - Int, the amount of nvme slots available on the motherboard, if 0 nvme support should not be assumed
"""

# Standard library imports
from os import getenv

# Related third party imports
from sqlalchemy import Column, String, Integer

# Local application/library specific imports
from models.base_model import BaseModel, Base

class Motherboard(BaseModel, Base):
    # For use with SQLalchemy, database table tied to class
    __tablename__ = "motherboards"
    
    if getenv("STORAGE_TYPE") == "db":
        Brand = Column(String(128), nullable=False)
        Model = Column(String(128), nullable=False)
        VideoOut = Column(String(128))
        Socket = Column(String(128))
        RAMType = Column(String(64))
        RAMSlots = Column(Integer())
        MAXRAMSPEED = Column(Integer())
        MINRAMSPEED = Column(Integer())
        NVMeSLOTS = Column(Integer())
    else:
        Brand = ""
        Model = ""
        VideoOut = ""
        USBOut = ""
        Socket = ""
        RAMType = ""
        RAMSlots = 0
        MAXRAMSPEED = 0
        MINRAMSPEED = 0
        NVMeSLOTS = 0

    def ConnectionList(self):
        '''
            Returns an array of strings, each string is a type of video connection, ie "VGA"
        '''
        data = self.VideoOut.split(',')
        return data