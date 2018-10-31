from . import api
from flask import jsonify


@api.route('/test', methods=['GET'])
def teset():
    return jsonify(
        {
            'code': 0,
            'msg': 'api test'
        }
    )