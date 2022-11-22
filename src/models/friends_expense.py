from sqlalchemy.sql import func

from models.group_friend import GroupFriend
from utilities import db


class FriendsExpense(db.Model):
    """Friends Expense Model"""

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    group_friend_id = db.Column(
        "groupFriendId", db.Integer, db.ForeignKey(GroupFriend.id)
    )
    amount = db.Column(db.Integer)
    created_at = db.Column("createdAt", db.DateTime, default=func.now())
    updated_at = db.Column("updatedAt", db.DateTime, onupdate=func.utc_timestamp())
