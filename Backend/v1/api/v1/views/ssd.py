#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Hocus Pocus SSD Views

This file contains views declorations for all routes dealing
with the SSD class. Each of these views responds to requests
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

@app_views.route('/ssds')
def return_ssds():
    ''' Returns jsonified array of all SSD class instances found in "storage" object
    '''
    SSDList = []
    SSDInfo = storage.all('SSD')
    for key, value in SSDInfo.items():
        ssd = value.to_dict()
        SSDList.append(ssd)
    return jsonify(SSDList)

@app_views.route('/ssds/<sku_id>', methods=['GET'], strict_slashes=False)
def get_ssds(sku_id):
    ''' Returns jsonified dicitionary of SSD class instances found in "storage" object with SKU matching "sku_id"
    '''
    if storage.get('SSD', sku_id) is None:
        abort(404)
    vari = storage.get('SSD', sku_id)
    return jsonify(vari.to_dict())