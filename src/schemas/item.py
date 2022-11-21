from models.item import User, Group, Friend, GroupFriend, FriendsExpense
from utilities import ma


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance=True


class GroupSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Group
        load_instance = True


class FriendSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Friend
        load_instance = True


class GroupFriendSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = GroupFriend
        load_instance = True


class FriendExpenseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = FriendsExpense
        load_instance = True
