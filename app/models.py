from app import db


class LowValueWhiteUser(db.Model):
    __tablename__ = 'low_quality_white_user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    createtime = db.Column(db.String(255))

    def to_json(self):
        json_post = {
            'phonenum': self.name,
            'createtime': self.createtime[:4] + '-' +
                          self.createtime[4:6] + '-' +
                          self.createtime[6:8] + ' ' +
                          self.createtime[8:10] + ':' +
                          self.createtime[10:12]
        }
        return json_post

    def __repr__(self):
        return '<Phonenum %r>' % self.name


class OrderTimesLimit(db.Model):
    __bind_key__ = 'ismp'
    __tablename__ = 'order_times_limit'
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.Integer)
    week = db.Column(db.Integer)
    month = db.Column(db.Integer)
    custom = db.Column(db.Integer)

    def to_json(self):
        return {
            'id': self.id,
            'day': self.day,
            'week': self.week,
            'month': self.month,
            'custom': self.custom
        }

    def __repr__(self):
        return '<OrderTimesLimit %r>' % self.id


class CpInfo(db.Model):
    __bind_key__ = 'ismp'
    __tablename__ = 'cp_info'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    level = db.Column(db.Integer)
    secret = db.Column(db.String(20))
    ip = db.Column(db.String(160))

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'level': self.level,
            'secret': self.secret,
            'ip': self.ip
        }

    def __repr__(self):
        return '<CpInfo %r>' % self.name


class ChargePoint(db.Model):
    __bind_key__ = 'ismp'
    __tablename__ = 'charge_point'

    id = db.Column(db.Integer, primary_key=True)
    pid = db.Column(db.String(30))
    secret = db.Column(db.String(30))
    description = db.Column(db.String(200))
    order_times_limit_id = db.Column(db.Integer)

    def to_json(self):
        return {
            'id': self.id,
            'pid': self.pid,
            'secret': self.secret,
            'description': self.description,
            'order_times_limit_id': self.order_times_limit_id
        }

    def __repr__(self):
        return '<ChargePoint %r>' % self.secret


class ProductInfo(db.Model):
    __bind_key__ = 'ismp'
    __tablename__ = 'product_info'

    id = db.Column(db.Integer, primary_key=True)
    sp_id = db.Column(db.String(10))
    product_id = db.Column(db.String(30))
    product_name = db.Column(db.String(100))
    price = db.Column(db.String(10))
    description = db.Column(db.Text)

    def to_json(self):
        return {
            'id': self.id,
            'sp_id': self.sp_id,
            'product_id': self.product_id,
            'product_name': self.product_name,
            'price': self.price,
            'description': self.description
        }

    def __repr__(self):
        return '<ProductInfo %r>' % self.product_name