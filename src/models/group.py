from sqlalchemy.sql import func

from models.user import User
from utilities import db


class Group(db.Model):
    """Group Model"""

    __tablename__ = "group"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column("userId", db.Integer, db.ForeignKey(User.id))
    name = db.Column(db.String)
    created_at = db.Column("createdAt", db.DateTime, default=func.now())
    updated_at = db.Column("updatedAt", db.DateTime, onupdate=func.utc_timestamp())
