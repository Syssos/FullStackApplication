#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Hocus Pocus Uncategorized Views

This file is used to handle all routes without a "home".
Routes for status codes, general server stats, and the likes
can all be found within this file.

Unlike the other view files, this one does not have caching in 
mind these endpoints were designed to return new, real time data
about the application.
"""

# Standard library imports
import random

# Related third party imports
from flask import jsonify, make_response

# Local application/library specific imports
from api.v1.views import app_views
from models import storage
from models import Ram
from models import Cable
from models import Case
from models import Motherboard

@app_views.route('/status')
def return_status():
        ''' Returns jsonified dictianary containing the api status
        '''
        return jsonify({"status": "OK"})

@app_views.route('/stats', strict_slashes=False)
def return_stats():
        ''' Returns jsonified dictianary containing the amount of each item based on the amount of class instances.
        '''
        stats = {
                'cables': storage.count('Cable'),
                'cases': storage.count('Case'),
                'cpus': storage.count('CPU'),
                'gpus': storage.count('GPU'),
                'monitors': storage.count('Monitor'),
                'motherboards': storage.count('Motherboard'),
                'memory': storage.count('Ram'),
                'psus': storage.count('PSU'),
                'ssds': storage.count('SSD')

        }
        return jsonify(stats)

@app_views.route('/items', strict_slashes=False)
def return_itemdata():
        ''' Returns jsonified array of each item pulled from storage object
        '''
        data = []
        for key, value in storage.all().items():
                data.append(value.to_dict())
        
        return jsonify(data)
        

@app_views.route('/items/featured', strict_slashes=False)
def return_featuredItems():
        ''' Returns jsonified array of 3 random objects contained within the storage object
        '''
        data = []
        for key, value in storage.all().items():
                data.append(value.to_dict())
        
        featured = []
        for x in range(3):
                featured.append(data[random.randint(0, len(data) -1 )])

        return jsonify(featured)

@app_views.route('/items/<sku_id>', methods=['GET'], strict_slashes=False)
def return_itemstat(sku_id):
        ''' Returns specific objects data based off "sku_id"
        '''
        for key, value in storage.all().items():
                if value.SKU == sku_id:
                        return jsonify(value.to_dict())
        return jsonify({"Error": "No Item Found"})
