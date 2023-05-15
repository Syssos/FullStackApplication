#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Hocus Pocus Cable Views

This file contains views declorations for all routes dealing
with the Cable class. Each of these views responds to requests
with JSON data as the response.

The routes within this file were initially created with the 
JS Caching library in mind. Caching this data on the frontend 
makes the overall application more efficient, and relives some 
stress on the API server.
"""

# Related third party imports
from flask import jsonify, make_response, abort

# Local application/library specific imports
from models import storage
from api.v1.views import app_views

@app_views.route('/cables')
def return_cables():
    ''' Returns jsonified array of all cable class instances found in "storage" object
    '''
    CableList = []
    CableInfo = storage.all('Cable')
    for key, value in CableInfo.items():
        cable = value.to_dict()
        CableList.append(cable)
    return jsonify(CableList)

@app_views.route('/cables/<sku_id>', methods=['GET'], strict_slashes=False)
def get_cable(sku_id):
    ''' Returns jsonified dicitionary of cable class instances found in "storage" object with SKU matching "sku_id"
    '''
    if storage.get('Cable', sku_id) is None:
        abort(404)
    vari = storage.get('Cable', sku_id)
    return jsonify(vari.to_dict())