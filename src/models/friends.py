from sqlalchemy.sql import func

from models.users import User
from utilities import db


class Friend(db.Model):
    """Friend Model"""

    __tablename__ = "friend"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column("userId", db.Integer, db.ForeignKey(User.id))
    name = db.Column(db.String)
    phone = db.Column(db.BigInteger)
    created_at = db.Column("createdAt", db.DateTime, default=func.now())
    updated_at = db.Column("updatedAt", db.DateTime, onupdate=func.utc_timestamp())
