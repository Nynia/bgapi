from app.models import CpInfo
from flask import jsonify, request
from app import db
from app.api import api


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


@api.route('/cp_info', methods=['GET'])
def get_cp_info():
    id = request.args.get('id')
    item = CpInfo.query.get(id)
    if item:
        return jsonify(
            {
                'code': '0',
                'msg': 'success',
                'data': item.to_json()
            }
        )
    else:
        return jsonify(
            {
                'code': '-1001',
                'msg': 'not exists'
            }
        )


@api.route('/cp_info', methods=['POST'])
def add_cp_info():
    id = request.form.get('id')
    name = request.form.get('name')
    level = request.form.get('level')

    if not level:
        level = 0
    if not id or not name:
        return jsonify(
            {
                'code': '-1003',
                'msg': 'param error'
            }
        )
    item = CpInfo.query.get(id)
    if item:
        return jsonify(
            {
                'code': '-1000',
                'msg': 'already exists'
            }
        )
    else:
        item = CpInfo()
        item.id = id
        item.name = name
        item.level = level

        db.session.add(item)
        db.session.commit()

        return jsonify(
            {
                'code': '0',
                'msg': 'success',
                'data': item.to_json()
            }
        )


@api.route('/cp_info', methods=['PUT'])
def alter_cp_info():
    id = request.form.get('id')
    name = request.form.get('name')
    level = request.form.get('level')

    if not id:
        return jsonify(
            {
                'code': '-1003',
                'msg': 'param error'
            }
        )
    else:
        item = CpInfo.query.get(id)
        if not item:
            return jsonify(
                {
                    'code': '-1001',
                    'msg': 'cp not exists'
                }
            )
        else:
            if name:
                item.name = name
            if level:
                item.level = level

            db.session.add(item)
            db.session.commit()

            return jsonify(
                {
                    'code': '0',
                    'msg': 'success',
                    'data': item.to_json()
                }
            )


@api.route('/cp_info/delete', methods=['POST'])
def delete_cp_info():
    id = request.form.get('id')
    item = CpInfo.query.get(id)
    if not item:
        return jsonify(
            {
                'code': '-1001',
                'msg': 'cp not exists'
            }
        )
    else:
        db.session.delete(item)
        db.session.commit()

        return jsonify(
            {
                'code': '0',
                'msg': 'delete success',
                'data': item.to_json()
            }
        )
