#!/usr/bin/python3
"""returns the status of the api"""


from api.v1.views import app_views
from flask import jsonify, make_response, abort
from models import storage

@app_views.route('/motherboards')
def return_mobos():
    ''' Returns api status
    '''
    MotherboardList = []
    MotherboardInfo = storage.all('Motherboard')
    for key, value in MotherboardInfo.items():
        motherboard = value.to_dict()
        MotherboardList.append(motherboard)
    return jsonify(MotherboardList)

@app_views.route('/motherboards/<sku_id>', methods=['GET'], strict_slashes=False)
def get_mobos(sku_id):
    """ Retrieves a City object
    """
    if storage.get('Motherboard', sku_id) is None:
        abort(404)
    vari = storage.get('Motherboard', sku_id)
    return jsonify(vari.to_dict())
