#!/usr/bin/python3
"""returns the status of the api"""


from api.v1.views import app_views
from flask import jsonify, make_response
from models import storage

@app_views.route('/cables')
def return_cables():
    ''' Returns api status
    '''
    CableList = []
    CableInfo = storage.all('Cable')
    for key, value in CableInfo.items():
        cable = value.to_dict()
        CableList.append(cable)
    return jsonify(CableList)

@app_views.route('/cables/<sku_id>', methods=['GET'], strict_slashes=False)
def get_cable(sku_id):
    """ Retrieves a City object
    """
    if storage.get('Cable', sku_id) is None:
        abort(404)
    vari = storage.get('Cable', sku_id)
    return jsonify(vari.to_dict())