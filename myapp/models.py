from .create_app import db


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), unique=True)
    lastname = db.Column(db.String(80), unique=True)
    nickname = db.Column(db.String(50))
    address = db.Column(db.Text)
    email = db.Column(db.String(100), unique=True, nullable=False)
    work = db.Column(db.String(100))

    def save(self):
        db.session.add(self)
        db.session.commit()