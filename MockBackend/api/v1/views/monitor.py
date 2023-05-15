#!/usr/bin/python3
"""returns the status of the api"""


from api.v1.views import app_views
from flask import jsonify, make_response
from models import storage

@app_views.route('/monitors')
def return_monitors():
    ''' Returns api status
    '''
    MonitorList = []
    MonitorInfo = storage.all('Monitor')
    for key, value in MonitorInfo.items():
        monitor = value.to_dict()
        MonitorList.append(monitor)
    return jsonify(MonitorList)

@app_views.route('/monitors/<sku_id>', methods=['GET'], strict_slashes=False)
def get_monitors(sku_id):
    """ Retrieves a Monitors object
    """
    if storage.get('Monitor', sku_id) is None:
        abort(404)
    vari = storage.get('Monitor', sku_id)
    return jsonify(vari.to_dict())