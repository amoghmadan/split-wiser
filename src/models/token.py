import binascii
import os

from sqlalchemy.sql import func

from models.user import User
from utilities import db


def generate_key():
    return binascii.hexlify(os.urandom(20)).decode()


class Token(db.Model):
    """Token Model"""

    __tablename__ = "token"

    key = db.Column(db.String, default=generate_key, primary_key=True)
    user_id = db.Column("userId", db.Integer, db.ForeignKey(User.id))
    created_at = db.Column("createdAt", db.DateTime, default=func.now())
    user = db.relationship("User", back_populates="token")
