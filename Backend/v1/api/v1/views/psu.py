#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Hocus Pocus PSU Views

This file contains views declorations for all routes dealing
with the PSU class. Each of these views responds to requests
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

@app_views.route('/psus')
def return_psus():
    """ Returns jsonified array of all PSU class instances found in "storage" object
    """
    PSUList = []
    PSUInfo = storage.all('PSU')
    for key, value in PSUInfo.items():
        psu = value.to_dict()
        PSUList.append(psu)
    return jsonify(PSUList)

@app_views.route('/psus/<sku_id>', methods=['GET'], strict_slashes=False)
def get_psus(sku_id):
    """ Returns jsonified dicitionary of PSU class instances found in "storage" object with SKU matching "sku_id"
    """
    if storage.get('PSU', sku_id) is None:
        abort(404)
    vari = storage.get('PSU', sku_id)
    return jsonify(vari.to_dict())