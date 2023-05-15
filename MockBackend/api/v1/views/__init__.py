#!/usr/bin/python3
"""init file with blueprint"""


from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

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