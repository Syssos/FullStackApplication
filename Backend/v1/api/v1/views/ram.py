#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Hocus Pocus Ram Views

This file contains views declorations for all routes dealing
with the Ram class. Each of these views responds to requests
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

@app_views.route('/memory')
def return_memory():
    """ Returns jsonified array of all Ram class instances found in "storage" object
    """
    MemoryList = []
    RamInfo = storage.all('Ram')
    for key, value in RamInfo.items():
        stick = value.to_dict()
        MemoryList.append(stick)
    return jsonify(MemoryList)

@app_views.route('/memory/<sku_id>', methods=['GET'], strict_slashes=False)
def get_memoryStick(sku_id):
    """ Returns jsonified dicitionary of Ram class instances found in "storage" object with SKU matching "sku_id"
    """
    if storage.get('Ram', sku_id) is None:
        abort(404)
    vari = storage.get('Ram', sku_id)
    return jsonify(vari.to_dict())