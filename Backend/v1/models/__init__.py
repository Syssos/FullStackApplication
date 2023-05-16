#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Hocus Pocus Model Initialization

This file is used to manage the storage object.
The storage object is responsible for retriving,
storing, changing, deleting, or modifing and data
on the application. This storage method can be
changed between a local file storage method utilizing
JSON, and a database storage method, making use of
MySQL and SQLalchemy.

The storage object is utilized as the vehicle for
interaction with the storage means. The classes dictionary
is used throughout the routes, and models files as a means
of tracking the type of classes used by the application.
"""

#!/usr/bin/python3
from models.engine import file_storage
from models.ram import Ram
from models.cable import Cable
from models.cases import Case
from models.cpu import CPU
from models.gpu import GPU
from models.gpu import GPU
from models.monitors import Monitor
from models.motherboard import Motherboard
from models.psu import PSU
from models.ssd import SSD
from models.user import User
from models.cart import Cart

storage = file_storage.FileStorage()

classes = {"Ram": Ram, "Cable": Cable, "Motherboard": Motherboard, 
           "Case": Case, "CPU": CPU, "GPU": GPU, "Monitor": Monitor, 
           "PSU": PSU, "SSD": SSD, "User": User, "Cart": Cart}

storage.reload()