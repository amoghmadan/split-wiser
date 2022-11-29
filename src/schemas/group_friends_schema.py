from models import GroupFriend
from utilities import ma


class GroupFriendSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = GroupFriend
        load_instance = True

