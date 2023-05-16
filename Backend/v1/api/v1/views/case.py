#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Hocus Pocus Case Views

This file contains views declorations for all routes dealing
with the Case class. Each of these views responds to requests
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

@app_views.route('/cases')
def return_cases():
    """ Returns jsonified array of all case class instances found in "storage" object
    """
    CaseList = []
    CaseInfo = storage.all('Case')
    for key, value in CaseInfo.items():
        case = value.to_dict()
        CaseList.append(case)
    return jsonify(CaseList)

@app_views.route('/cases/<sku_id>', methods=['GET'], strict_slashes=False)
def get_cases(sku_id):
    """ Returns jsonified dicitionary of case class instances found in "storage" object with SKU matching "sku_id"
    """
    if storage.get('Case', sku_id) is None:
        abort(404)
    vari = storage.get('Case', sku_id)
    return jsonify(vari.to_dict())