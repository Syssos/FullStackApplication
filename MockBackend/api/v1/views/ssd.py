#!/usr/bin/python3
"""returns the status of the api"""


from api.v1.views import app_views
from flask import jsonify, make_response
from models import storage

@app_views.route('/ssds')
def return_ssds():
    ''' Returns api status
    '''
    SSDList = []
    SSDInfo = storage.all('SSD')
    for key, value in SSDInfo.items():
        ssd = value.to_dict()
        SSDList.append(ssd)
    return jsonify(SSDList)

@app_views.route('/ssds/<sku_id>', methods=['GET'], strict_slashes=False)
def get_ssds(sku_id):
    """ Retrieves a City object
    """
    if storage.get('SSD', sku_id) is None:
        abort(404)
    vari = storage.get('SSD', sku_id)
    return jsonify(vari.to_dict())