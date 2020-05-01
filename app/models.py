from app import db

class ewmodel(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    serial = db.Column(db.String(6), index=True, unique=True)
    batteries = db.Column(db.Integer)
    holders = db.Column(db.Integer)
    plates = db.relationship('platemodel', lazy='dynamic')
    indicators = db.relationship('indicatormodel', lazy='dynamic')

    def __repr__(self):
        return '<EW for bomb: {}>'.format(self.serial)

class platemodel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    RJ = db.Column(db.Boolean, default=False)
    PS2 = db.Column(db.Boolean, default=False)
    DVI = db.Column(db.Boolean, default=False)
    RCA = db.Column(db.Boolean, default=False)
    parallel = db.Column(db.Boolean, default=False)
    serial = db.Column(db.Boolean, default=False)
    bomb_id = db.Column(db.Integer, db.ForeignKey('ewmodel.id'))

    def __repr__(self):
        p = []
        if self.RJ:
            p.append('RJ-45')
        if self.PS2:
            p.append('PS2')
        if self.DVI:
            p.append('DVI-D')
        if self.RCA:
            p.append('Sterio RCA')
        if self.parallel:
            p.append('Parallel')
        if self.serial:
            p.append('Serial')
        return p

class indicatormodel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(3))
    light = db.Column(db.Boolean)
    bomb_id = db.Column(db.Integer, db.ForeignKey('ewmodel.id'))

    def __repr__(self):
        return [self.light, self.label]
