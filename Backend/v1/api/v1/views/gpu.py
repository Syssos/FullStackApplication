#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Hocus Pocus GPU Views

This file contains views declorations for all routes dealing
with the GPU class. Each of these views responds to requests
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

@app_views.route('/gpus')
def return_gpus():
    ''' Returns jsonified array of all GPU class instances found in "storage" object
    '''
    GPUList = []
    GPUInfo = storage.all('GPU')
    for key, value in GPUInfo.items():
        gpu = value.to_dict()
        GPUList.append(gpu)
    return jsonify(GPUList)

@app_views.route('/gpus/<sku_id>', methods=['GET'], strict_slashes=False)
def get_gpus(sku_id):
    ''' Returns jsonified dicitionary of GPU class instances found in "storage" object with SKU matching "sku_id"
    '''
    if storage.get('GPU', sku_id) is None:
        abort(404)
    vari = storage.get('GPU', sku_id)
    return jsonify(vari.to_dict())