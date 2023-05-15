#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Hocus Pocus Motherboard Views

This file contains views declorations for all routes dealing
with the Motherboard class. Each of these views responds to requests
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

@app_views.route('/motherboards')
def return_mobos():
    ''' Returns jsonified array of all Motherboard class instances found in "storage" object
    '''
    MotherboardList = []
    MotherboardInfo = storage.all('Motherboard')
    for key, value in MotherboardInfo.items():
        motherboard = value.to_dict()
        MotherboardList.append(motherboard)
    return jsonify(MotherboardList)

@app_views.route('/motherboards/<sku_id>', methods=['GET'], strict_slashes=False)
def get_mobos(sku_id):
    ''' Returns jsonified dicitionary of Motherboard class instances found in "storage" object with SKU matching "sku_id"
    '''
    if storage.get('Motherboard', sku_id) is None:
        abort(404)
    vari = storage.get('Motherboard', sku_id)
    return jsonify(vari.to_dict())
