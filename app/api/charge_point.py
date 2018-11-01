from app.models import ChargePoint, ProductInfo
from flask import jsonify, request
from app import db
from . import api


@api.route('/charge_points', methods=['GET'])
def get_charge_points():
    items = ChargePoint.query.all()
    return jsonify(
        {
            'code': '0',
            'msg': 'success',
            'data': [g.to_json() for g in items]
        }
    )


@api.route('/charge_point', methods=['GET'])
def get_charge_point():
    id = request.args.get('id')
    pid = request.args.get('pid')

    if id:
        item = ChargePoint.query.get(int(id))
        return jsonify(
            {
                'code': '0',
                'msg': 'success',
                'data': item.to_json()
            }
        )
    elif pid:
        items = ChargePoint.query.filter_by(pid=pid).all()
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


@api.route('/charge_point', methods=['POST'])
def add_charge_point():
    pass


@api.route('/charge_point', methods=['PUT'])
def alter_charge_point():
    product_id = request.form.get('p_id')
    otl_id = request.form.get('otl_id')
    cp_id = request.form.get('cp_id')

    if product_id and otl_id:
        item = ChargePoint.query.filter_by(pid=product_id).first()
        if item:
            item.order_times_limit_id = otl_id
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
                    'code': '-1001',
                    'msg': 'not exists'
                }
            )
    elif cp_id:
        result = []
        product_items = ProductInfo.query.filter_by(sp_id=cp_id).all()
        for item in product_items:
            pid = item.product_id
            charge_item = ChargePoint.query.filter_by(pid=pid).first()
            if charge_item:
                charge_item.order_times_limit_id = otl_id
                db.session.add(item)
                result.append(charge_item)
        db.session.commit()
        return jsonify(
            {
                'code': '0',
                'msg': 'success',
                'data': [g.to_json() for g in result]
            }
        )
    else:
        return jsonify(
            {
                'code': '-1003',
                'msg': 'param error'
            }
        )


@api.route('/charge_points', methods=['DELETE'])
def delete_charge_point():
    pass
