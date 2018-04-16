from . import db


# 用户对象
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False, unique=True)
    username = db.Column(db.String(255), index=True)
    age = db.Column(db.Integer)
    phone = db.Column(db.String(255))
