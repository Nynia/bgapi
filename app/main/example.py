from . import main
from flask import jsonify


@main.route('/test', methods=['GET'])
def teset():
    return jsonify(
        {
            'code': 0,
            'msg':'main test'
        }
    )