from app.models import CpInfo
from flask import jsonify, request
from app import db
from . import api
import re


@api.route('/cp_infos', methods=['GET'])
def get_cp_infos():
    items = CpInfo.query.all()
    return jsonify(
        {
            'code': '0',
            'msg': 'success',
            'data': [g.to_json() for g in items]
        }
    )


@api.route('/cp_info', methods=['POST'])
def add_cp_info():
    pass


@api.route('/cp_info', methods=['PUT'])
def alter_cp_info():
    pass


@api.route('/cp_info', methods=['DELETE'])
def delete_cp_info():
    pass
