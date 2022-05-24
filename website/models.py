from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


# Parent
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(10), unique=True)
    accountType = db.Column(db.String(10))  # user/admin

    tickets = db.relationship('Ticket')
    notifications = db.relationship('Notification')


# Childs
class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(100))
    status = db.Column(db.String(20))  # store success or error
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    desc = db.Column(db.String(1000))
    username = db.Column(db.String(15))
    status = db.Column(db.String(20))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
