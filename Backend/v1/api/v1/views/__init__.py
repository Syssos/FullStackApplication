#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Hocus Pocus Views Initialization

This file is responsible for collecting all route views for the
API, each one of these files correspondes to a specific class
and the work that needs to be done to display its data.

This file should not include any route definitions, it should just
build the Blueprint, then import desired route definitions from an 
additional file. This helps maintain organization and code 
read-ability.
"""

# Related third party imports
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Local application/library specific imports
from api.v1.views.index import *
from api.v1.views.ram import *
from api.v1.views.cable import *
from api.v1.views.case import *
from api.v1.views.cpu import *
from api.v1.views.gpu import *
from api.v1.views.monitor import *
from api.v1.views.motherboard import *
from api.v1.views.psu import *
from api.v1.views.ssd import *