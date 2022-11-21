from utilities import db


class User(db.Model):
    """User Model"""
    id = db.Column(db.Integer)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    phone = db.Column(db.BigInteger)


class Group(db.Model):
    """Group Model"""
    id = db.Column(db.Integer)
    name = db.Column(db.String)
    userid = db.Column(db.Integer, db.ForeignKey(User.id))


class Friend(db.Model):
    """Friend Model"""
    id = db.Column(db.Integer)
    name = db.Column(db.String)
    phone = db.Column(db.BigInteger)
    userid = db.Column(db.Integer, db.FoeignKey(User.id))


class GroupFriend(db.Model):
    """Group Friend Model"""
    id = db.Column(db.Integer, primary_key=True)
    groupid = db.Column(db.Integer, db.ForeignKey(Group.id))
    friendid = db.Column(db.Integer, db.ForeignKey(Friend.id))
    amount = db.Column(db.Integer)
    expense = db.Column(db.String)


class FriendsExpense(db.Model):
    """Friends Expense Model"""
    id = db.Column(db.Integer, primary_key=True)
    groupfriendid = db.Column(db.Integer, db.ForeignKey(GroupFriend.id))
    amount = db.Column(db.Integer)
