from sqlalchemy.sql import func

from models.user import User
from utilities import db


class Token(db.Model):
    """Token Model"""

    __tablename__ = "token"

    user_id = db.Column("userId", db.Integer, db.ForeignKey(User.id), primary_key=True)
    user = db.relationship("User", back_populates="token")
    key = db.Column(db.String)
    created_at = db.Column("createdAt", db.DateTime, default=func.now())
