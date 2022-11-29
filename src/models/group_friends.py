from sqlalchemy.sql import func

from models.friends import Friend
from models.groups import Group
from utilities import db


class GroupFriend(db.Model):
    """Group Friend Model"""

    __tablename__ = "groupFriend"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    group_id = db.Column("groupId", db.Integer, db.ForeignKey(Group.id))
    friend_id = db.Column("friendId", db.Integer, db.ForeignKey(Friend.id))
    amount = db.Column(db.Integer)
    expense = db.Column(db.String)
    created_at = db.Column("createdAt", db.DateTime, default=func.now())
    updated_at = db.Column("updatedAt", db.DateTime, onupdate=func.utc_timestamp())
