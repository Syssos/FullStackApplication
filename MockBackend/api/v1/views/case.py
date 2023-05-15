#!/usr/bin/python3
"""returns the status of the api"""


from api.v1.views import app_views
from flask import jsonify, make_response
from models import storage

@app_views.route('/cases')
def return_cases():
    ''' Returns api status
    '''
    CaseList = []
    CaseInfo = storage.all('Case')
    for key, value in CaseInfo.items():
        case = value.to_dict()
        CaseList.append(case)
    return jsonify(CaseList)

@app_views.route('/cases/<sku_id>', methods=['GET'], strict_slashes=False)
def get_cases(sku_id):
    """ Retrieves a Case object
    """
    if storage.get('Case', sku_id) is None:
        abort(404)
    vari = storage.get('Case', sku_id)
    return jsonify(vari.to_dict())