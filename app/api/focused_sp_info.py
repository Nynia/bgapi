from app.models import FocusedSpInfo
from flask import jsonify, request
from app import db
from . import api


@api.route('/focused_sp_infos', methods=['GET'])
def get_all_spinfos():
    items = FocusedSpInfo.query.all()
    return jsonify(
        {
            'code': '0',
            'msg': 'success',
            'data': [g.to_json() for g in items]
        }
    )


@api.route('/focused_sp_info', methods=['GET'])
def get_sp_info():
    spid = request.args.get('spid')
    item = FocusedSpInfo.query.get(spid)
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


@api.route('/focused_sp_info', methods=['POST'])
def add_sp_info():
    spid = request.form.get('spid')
    spname = request.form.get('spname')
    accessno = request.form.get('accessno')

    if spid and spname and accessno:
        item = FocusedSpInfo.query.get(spid)
        if item:
            return jsonify(
                {
                    'code': '-1000',
                    'msg': 'already exists'
                }
            )
        else:
            item = FocusedSpInfo()
            item.spname = spname
            item.spid = spid
            item.accessno = accessno

            db.session.add(item)
            db.session.commit()

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
                'code': '-1003',
                'msg': 'param error'
            }
        )


@api.route('/focused_sp_info', methods=['DELETE'])
def delete_sp_info():
    spid = request.form.get('spid')
    item = FocusedSpInfo.query.get(spid)
    if item:
        db.session.delete(item)
        db.session.commit()
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
