from models import FriendsExpense
from utilities import ma


class FriendExpenseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = FriendsExpense
        load_instance = True
