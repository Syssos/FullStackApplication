#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Hocus Pocus CPU Views

This file contains views declorations for all routes dealing
with the CPU class. Each of these views responds to requests
with JSON data as the response.

The routes within this file were initially created with the 
JS Caching library in mind. Caching this data on the frontend 
makes the overall application more efficient, and relives some 
stress on the API server.
"""

# Related third party imports
from flask import jsonify, make_response, abort

# Local application/library specific imports
from api.v1.views import app_views
from models import storage

@app_views.route('/cpus')
def return_cpus():
    """ Returns jsonified array of all CPU class instances found in "storage" object
    """
    CPUList = []
    CPUInfo = storage.all('CPU')
    for key, value in CPUInfo.items():
        cpu = value.to_dict()
        CPUList.append(cpu)
    return jsonify(CPUList)

@app_views.route('/cpus/<sku_id>', methods=['GET'], strict_slashes=False)
def get_cpus(sku_id):
    """ Returns jsonified dicitionary of CPU class instances found in "storage" object with SKU matching "sku_id"
    """
    if storage.get('CPU', sku_id) is None:
        abort(404)
    vari = storage.get('CPU', sku_id)
    return jsonify(vari.to_dict())