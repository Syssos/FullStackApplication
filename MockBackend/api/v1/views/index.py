#!/usr/bin/python3
"""returns the status of the api"""


import random
from api.v1.views import app_views
from flask import jsonify, make_response
from models import storage
from models import Ram
from models import Cable
from models import Case
from models import Motherboard

@app_views.route('/status')
def return_status():
        ''' Returns api status
        '''

        return jsonify({"status": "OK"})

@app_views.route('/stats', strict_slashes=False)
def return_stats():
        ''' stats
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
        ''' stats
        '''
        data = []
        for key, value in storage.all().items():
                data.append(value.to_dict())
        
        return jsonify(data)
        

@app_views.route('/items/featured', strict_slashes=False)
def return_featuredItems():
        ''' stats
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
        ''' stats
        '''        
        for key, value in storage.all().items():
                if value.SKU == sku_id:
                        return jsonify(value.to_dict())
        return jsonify({"Error": "No Item Found"})
