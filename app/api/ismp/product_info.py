from app.models import ProductInfo, ChargePoint
from flask import jsonify, request
from app import db
from app.api import api


@api.route('/product_info', methods=['GET'])
def get_product_info():
    spid = request.args.get('spid')
    productid = request.args.get('productid')
    print spid
    if spid:
        items = ProductInfo.query.filter_by(sp_id=spid).all()
        return jsonify(
            {
                'code': '0',
                'msg': 'success',
                'data': [g.to_json() for g in items]
            }
        )
    elif productid:
        item = ProductInfo.query.filter_by(product_id=productid).first()
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
                    'msg': 'product not exists'
                }
            )
    else:
        return jsonify(
            {
                'code': '-1003',
                'msg': 'param error'
            }
        )


@api.route('/product_info', methods=['POST'])
def add_product_info():
    spid = request.form.get('spid')
    productid = request.form.get('productid')
    productname = request.form.get('productname')
    price = request.form.get('price')

    if not productid or not spid:
        return jsonify(
            {
                'code': '-1003',
                'msg': 'param error'
            }
        )
    else:
        item = ProductInfo.query.filter_by(product_id=productid).first()
        if item:
            return jsonify(
                {
                    'code': '-1002',
                    'msg': 'productid exists'
                }
            )
        else:
            item = ProductInfo()
            item.product_id = productid
            item.sp_id = spid
            item.product_name = productname
            item.price = price

            db.session.add(item)
            db.session.commit()

            return jsonify(
                {
                    'code': '0',
                    'msg': 'success',
                    'data': item.to_json()
                }
            )


@api.route('/product_info', methods=['PUT'])
def alter_product_info():
    spid = request.form.get('spid')
    productid = request.form.get('productid')
    productname = request.form.get('productname')
    price = request.form.get('price')

    if not productid:
        return jsonify(
            {
                'code': '-1003',
                'msg': 'param error'
            }
        )
    else:
        item = ProductInfo.query.filter_by(product_id=productid).first()
        if not item:
            return jsonify(
                {
                    'code': '-1001',
                    'msg': 'product not exists'
                }
            )
        else:
            if productname:
                item.product_name = productname
            if price:
                item.price = price
            if spid:
                item.sp_id = spid

            db.session.add(item)
            db.session.commit()

            return jsonify(
                {
                    'code': '0',
                    'msg': 'success',
                    'data': item.to_json()
                }
            )


@api.route('/product_info/delete', methods=['POST'])
def delete_product_info():
    productid = request.form.get('productid')
    item = ProductInfo.query.filter_by(product_id=productid).first()
    if not item:
        return jsonify(
            {
                'code': '-1001',
                'msg': 'product not exists'
            }
        )
    else:
        db.session.delete(item)
        # delete charge_point
        db.session.commit()

        return jsonify(
            {
                'code': '0',
                'msg': 'success',
                'data': item.to_json()
            }
        )
