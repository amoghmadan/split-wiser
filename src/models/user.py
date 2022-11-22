from sqlalchemy.sql import func

from utilities import db


class User(db.Model):
    """User Model"""

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column("firstName", db.String)
    last_name = db.Column("lastName", db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    phone = db.Column(db.BigInteger)
    created_at = db.Column("createdAt", db.DateTime, default=func.now())
    updated_at = db.Column("updatedAt", db.DateTime, onupdate=func.utc_timestamp())
    token = db.relationship("Token", back_populates="user")
