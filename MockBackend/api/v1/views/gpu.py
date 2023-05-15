#!/usr/bin/python3
"""returns the status of the api"""


from api.v1.views import app_views
from flask import jsonify, make_response
from models import storage

@app_views.route('/gpus')
def return_gpus():
    ''' Returns api status
    '''
    GPUList = []
    GPUInfo = storage.all('GPU')
    for key, value in GPUInfo.items():
        gpu = value.to_dict()
        GPUList.append(gpu)
    return jsonify(GPUList)

@app_views.route('/gpus/<sku_id>', methods=['GET'], strict_slashes=False)
def get_gpus(sku_id):
    """ Retrieves a Case object
    """
    if storage.get('GPU', sku_id) is None:
        abort(404)
    vari = storage.get('GPU', sku_id)
    return jsonify(vari.to_dict())