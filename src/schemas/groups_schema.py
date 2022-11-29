from models import Group
from utilities import ma

class GroupSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Group
        load_instance = True

