from app.models import OrderTimesLimit
from flask import jsonify, request
from app import db
from . import api
import re


@api.route('/order_times_limits', methods=['GET'])
def get_all_otls():
    items = OrderTimesLimit.query.all()
    return jsonify(
        {
            'code': '0',
            'msg': 'success',
            'data': [g.to_json() for g in items]
        }
    )


@api.route('/order_times_limit', methods=['POST'])
def add_otl():
    day = request.form.get('day', '-1')
    week = request.form.get('week', '-1')
    month = request.form.get('month', '-1')
    custom = request.form.get('custom', '-1')

    print day, week, month
    pattern = re.compile("-?[1-9]\d?")
    if day == '-1' and week == '-1' and month == '-1':
        return jsonify(
            {
                'code': '-1003',
                'msg': 'param error'
            }
        )
    if re.match(pattern, day) and \
            re.match(pattern, week) and \
            re.match(pattern, month):
        item = OrderTimesLimit()
        item.day = day
        item.week = week
        item.month = month
        item.custom = custom
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
                'code': '-1002',
                'msg': 'format error'
            }
        )


@api.route('/order_times_limit', methods=['DELETE'])
def delete_otl():
    id = request.form.get('id')
    if id:
        if not re.match('\d+', id):
            return jsonify(
                {
                    'code': '-1002',
                    'msg': 'format error'
                }
            )
        item = OrderTimesLimit.query.get(int(id))
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

    else:
        return jsonify(
            {
                'code': '-1003',
                'msg': 'param error'
            }
        )

