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


class User(db.Model):
    __bind_key__ = 'ismp'
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
