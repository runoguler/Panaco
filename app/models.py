from app import db

class Medicine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    dosage = db.Column(db.Integer)

    def __repr__(self):
        return '<Medicine: {}, Dosage: {}>'.format(self.name, self.dosage)