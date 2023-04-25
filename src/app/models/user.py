from flask_login import UserMixin
from app.extensions import db


class User(UserMixin, db.Model):
    """User Database Model"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password_hash = db.Column(db.Text)

    def __repr__(self):
        return f'<User "{self.username}">'
