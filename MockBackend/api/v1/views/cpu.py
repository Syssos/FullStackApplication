#!/usr/bin/python3
"""returns the status of the api"""


from api.v1.views import app_views
from flask import jsonify, make_response
from models import storage

@app_views.route('/cpus')
def return_cpus():
    ''' Returns api status
    '''
    CPUList = []
    CPUInfo = storage.all('CPU')
    for key, value in CPUInfo.items():
        cpu = value.to_dict()
        CPUList.append(cpu)
    return jsonify(CPUList)

@app_views.route('/cpus/<sku_id>', methods=['GET'], strict_slashes=False)
def get_cpus(sku_id):
    """ Retrieves a Case object
    """
    if storage.get('CPU', sku_id) is None:
        abort(404)
    vari = storage.get('CPU', sku_id)
    return jsonify(vari.to_dict())