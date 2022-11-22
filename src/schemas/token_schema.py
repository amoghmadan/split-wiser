from models import Token

from utilities import ma


class TokenSchema(ma.SQLAlchemySchema):
    """Token Schema"""

    class Meta:
        model = Token
        load_instance = True


class LoginSchema(ma.Schema):
    """Login Schema"""

    email = ma.Str(load=True)
    password = ma.Str(load=True)
