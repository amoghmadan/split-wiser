from marshmallow import fields

from models import Token
from utilities import ma


class LoginSchema(ma.Schema):
    """Login Schema"""

    email = fields.Str(load_only=True)
    password = fields.Str(load_only=True)


class TokenSchema(ma.SQLAlchemySchema):
    """Token Schema"""

    class Meta:
        model = Token
        load_instance = True
