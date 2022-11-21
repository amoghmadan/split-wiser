from sqlalchemy.sql import func

from utilities import db


class User(db.Model):
    """User Model"""

    id = db.Column(db.Integer)
    first_name = db.Column("firstName", db.String)
    last_name = db.Column("lastName", db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    phone = db.Column(db.BigInteger)
    created_at = db.Column("createdAt", db.DateTime, default=func.now())
    updated_at = db.Column("updatedAt", db.DateTime, onupdate=func.utc_timestamp())


class Group(db.Model):
    """Group Model"""

    id = db.Column(db.Integer)
    user_id = db.Column("userId", db.Integer, db.ForeignKey(User.id))
    name = db.Column(db.String)
    created_at = db.Column("createdAt", db.DateTime, default=func.now())
    updated_at = db.Column("updatedAt", db.DateTime, onupdate=func.utc_timestamp())


class Friend(db.Model):
    """Friend Model"""

    id = db.Column(db.Integer)
    user_id = db.Column("userId", db.Integer, db.FoeignKey(User.id))
    name = db.Column(db.String)
    phone = db.Column(db.BigInteger)
    created_at = db.Column("createdAt", db.DateTime, default=func.now())
    updated_at = db.Column("updatedAt", db.DateTime, onupdate=func.utc_timestamp())


class GroupFriend(db.Model):
    """Group Friend Model"""

    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column("groupId", db.Integer, db.ForeignKey(Group.id))
    friend_id = db.Column("friendId", db.Integer, db.ForeignKey(Friend.id))
    amount = db.Column(db.Integer)
    expense = db.Column(db.String)
    created_at = db.Column("createdAt", db.DateTime, default=func.now())
    updated_at = db.Column("updatedAt", db.DateTime, onupdate=func.utc_timestamp())


class FriendsExpense(db.Model):
    """Friends Expense Model"""

    id = db.Column(db.Integer, primary_key=True)
    group_friend_id = db.Column(
        "groupFriendId", db.Integer, db.ForeignKey(GroupFriend.id)
    )
    amount = db.Column(db.Integer)
    created_at = db.Column("createdAt", db.DateTime, default=func.now())
    updated_at = db.Column("updatedAt", db.DateTime, onupdate=func.utc_timestamp())
