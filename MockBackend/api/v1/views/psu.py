#!/usr/bin/python3
"""returns the status of the api"""


from api.v1.views import app_views
from flask import jsonify, make_response
from models import storage

@app_views.route('/psus')
def return_psus():
    ''' Returns api status
    '''
    PSUList = []
    PSUInfo = storage.all('PSU')
    for key, value in PSUInfo.items():
        psu = value.to_dict()
        PSUList.append(psu)
    return jsonify(PSUList)

@app_views.route('/psus/<sku_id>', methods=['GET'], strict_slashes=False)
def get_psus(sku_id):
    """ Retrieves a Case object
    """
    if storage.get('PSU', sku_id) is None:
        abort(404)
    vari = storage.get('PSU', sku_id)
    return jsonify(vari.to_dict())