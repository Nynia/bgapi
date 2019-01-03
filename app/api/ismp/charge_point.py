from app.models import ChargePoint, ProductInfo
from flask import jsonify, request
from app import db
from app.api import api
import datetime
import hashlib


@api.route('/charge_point', methods=['GET'])
def get_charge_point():
    id = request.args.get('id')
    productid = request.args.get('productid')

    if id:
        item = ChargePoint.query.get(int(id))
        return jsonify(
            {
                'code': '0',
                'msg': 'success',
                'data': item.to_json() if item else None
            }
        )
    elif productid:
        items = ChargePoint.query.filter_by(pid=productid).all()
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
    productid = request.form.get('productid')
    day_limit = request.form.get('day_limit')
    week_limit = request.form.get('week_limit')
    month_limit = request.form.get('month_limit')
    desc = request.form.get('desc')

    # gen secret
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    m2 = hashlib.md5()
    m2.update(timestamp)
    secret = m2.hexdigest()[:12]
    print secret

    item = ChargePoint()
    item.pid = productid
    item.secret = secret
    item.day_limit = day_limit if day_limit else 0
    item.week_limit = week_limit if week_limit else 0
    item.month_limit = month_limit if month_limit else 0
    item.description = desc if desc else ''

    db.session.add(item)
    db.session.commit()

    return jsonify(
        {
            'code': '0',
            'msg': 'success',
            'data': item.to_json() if item else None
        }
    )


@api.route('/charge_point', methods=['PUT'])
def alter_charge_point():
    id = request.form.get('id')
    desc = request.form.get('desc')
    day_limit = request.form.get('day_limit')
    week_limit = request.form.get('week_limit')
    month_limit = request.form.get('month_limit')

    if not id:
        return jsonify(
            {
                'code': '-1003',
                'msg': 'param error'
            }
        )
    else:
        item = ChargePoint.query.get(int(id))
        if item:
            if desc:
                item.description = desc
            if day_limit:
                item.day_limit = day_limit
            if week_limit:
                item.week_limit = week_limit
            if month_limit:
                item.month_limit = month_limit

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


@api.route('/charge_point/delete', methods=['POST'])
def delete_charge_point():
    id = request.form.get('id')
    print id
    if not id:
        return jsonify(
            {
                'code': '-1003',
                'msg': 'param error'
            }
        )
    else:
        item = ChargePoint.query.get(int(id))
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
