from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login

class Movies_Database (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, index=True, unique=True)
    score = db.Column(db.Float, index=True)
    type = db.Column(db.String, index=True)

    def __repr__(self):
        return "{} {} {}".format(self.name, self.score, self.type)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, index=True, unique=True)
    email = db.Column(db.String, index=True, unique=True)
    password = db.Column(db.String, unique=True)

    def set_pswd(self, pswd):
        self.password_hash = generate_password_hash(pswd)

    def check_pswd(self, pswd):
        return check_password_hash(self.password_hash, pswd)