#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Hocus Pocus Monitor Views

This file contains views declorations for all routes dealing
with the Monitor class. Each of these views responds to requests
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

@app_views.route('/monitors')
def return_monitors():
    ''' Returns jsonified array of all Monitor class instances found in "storage" object
    '''
    MonitorList = []
    MonitorInfo = storage.all('Monitor')
    for key, value in MonitorInfo.items():
        monitor = value.to_dict()
        MonitorList.append(monitor)
    return jsonify(MonitorList)

@app_views.route('/monitors/<sku_id>', methods=['GET'], strict_slashes=False)
def get_monitors(sku_id):
    ''' Returns jsonified dicitionary of Monitor class instances found in "storage" object with SKU matching "sku_id"
    '''
    if storage.get('Monitor', sku_id) is None:
        abort(404)
    vari = storage.get('Monitor', sku_id)
    return jsonify(vari.to_dict())