#!/usr/bin/python3
"""returns the status of the api"""


from api.v1.views import app_views
from flask import jsonify, make_response
from models import storage

@app_views.route('/memory')
def return_memory():
    ''' Returns api status
    '''
    MemoryList = []
    RamInfo = storage.all('Ram')
    for key, value in RamInfo.items():
        stick = value.to_dict()
        MemoryList.append(stick)
    return jsonify(MemoryList)

@app_views.route('/memory/<sku_id>', methods=['GET'], strict_slashes=False)
def get_memoryStick(sku_id):
    """ Retrieves a City object
    """
    if storage.get('Ram', sku_id) is None:
        abort(404)
    vari = storage.get('Ram', sku_id)
    return jsonify(vari.to_dict())