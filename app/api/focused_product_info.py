from app.models import FocusedSpInfo, FocusedProductInfo
from flask import jsonify, request
from app import db
from . import api


@api.route('/focused_product_infos', methods=['GET'])
def get_all_product_infos():
    pass


@api.route('/focused_product_info', methods=['GET'])
def get_focused_product_info():
    spid = request.args.get('spid')
    serviceid = request.args.get('serviceid')

    if spid:
        items = FocusedProductInfo.query.filter_by(spid=spid).all()
        return jsonify(
            {
                'code': '0',
                'msg': 'success',
                'data': [g.to_json() for g in items]
            }
        )
    elif serviceid:
        item = FocusedProductInfo.query.get(serviceid)
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
    else:
        return jsonify(
            {
                'code': '-1003',
                'msg': 'param error'
            }
        )


@api.route('/focused_product_info', methods=['POST'])
def add_focused_product_info():
    serviceid = request.form.get('serviceid')
    servicename = request.form.get('servicename')
    spid = request.form.get('spid')
    orderflag = request.form.get('orderflag')

    item = FocusedProductInfo.query.get(serviceid)
    if item:
        return jsonify(
            {
                'code': '-1000',
                'msg': 'already exists'
            }
        )
    else:
        spinfo_item = FocusedSpInfo.query.get(spid)
        if not spinfo_item:
            return jsonify(
                {
                    'code': '-1001',
                    'msg': 'sp not exists'
                }
            )
        item = FocusedProductInfo()
        item.serviceid = serviceid
        item.servicename = servicename
        item.orderflag = orderflag
        item.spid = spid

        db.session.add(item)
        db.session.commit()

        return jsonify(
            {
                'code': '0',
                'msg': 'success',
                'data': item.to_json()
            }
        )


@api.route('/focused_product_info', methods=['DELETE'])
def delete_focused_product_info():
    serviceid = request.form.get('serviceid')
    spid = request.form.get('spid')
    if serviceid:
        item = FocusedProductInfo.query.get(serviceid)
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
    elif spid:
        items = FocusedProductInfo.query.filter_by(spid=spid).all()
        for item in items:
            db.session.delete(item)
        db.session.commit()
        return jsonify(
            {
                'code': '0',
                'msg': 'success',
                'data': [g.to_json() for g in items]
            }
        )
    else:
        return jsonify(
            {
                'code': '-1003',
                'msg': 'param error'
            }
        )
