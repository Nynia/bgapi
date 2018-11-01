from app.models import LowValueWhiteUser
from flask import jsonify
from app import db
from datetime import datetime
from . import api
import re


@api.route('/low_value/list')
def get_all():
    items = LowValueWhiteUser.query.all()
    return jsonify([g.to_json() for g in items])


@api.route('/low_value/delete/<name>', methods=['GET'])
def delete(name):
    item = LowValueWhiteUser.query.filter_by(name=name).first()
    if item:
        db.session.delete(item)
        db.session.commit()
        return jsonify(
            {
                'msg': 'sccess',
                'data': item.to_json()
            }
        )
    else:
        return jsonify(
            {
                'msg': 'phonenum not exist'
            }
        )


@api.route('/low_value/add/<name>', methods=['GET'])
def add(name):
    if not re.match('1\d{10}', name):
        return jsonify(
            {
                'msg': 'wrong phonenum',
            }
        )
    item = LowValueWhiteUser.query.filter_by(name=name).first()
    if item:
        return jsonify(
            {
                'msg': 'phonenum exist',
            }
        )
    item = LowValueWhiteUser()
    item.name = name
    item.createtime = datetime.now().strftime('%Y%m%d%H%M%S')
    db.session.add(item)
    db.session.commit()
    return jsonify(
        {
            'msg': 'success',
            'data': item.to_json()
        }
    )
