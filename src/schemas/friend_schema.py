from models import Friend
from utilities import ma


class FriendSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Friend
        load_instance = True
