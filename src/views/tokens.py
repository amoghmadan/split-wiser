import binascii
import os

from flask import views, request
from sqlalchemy.exc import IntegrityError

from models import Token, User
from schemas import TokenSchema
from utilities import db


class TokenViewSet(views.MethodView):
    model = Token
    schema_class = TokenSchema

    @classmethod
    def generate_key(cls):
        """It will generate the token"""
        return binascii.hexlify(os.urandom(20)).decode()

    def get(self, *args, **kwargs):

        auth = request.authorization
        if not auth or not auth.username or not auth.password:
            return {"message": "could not verify"}

        instance = User.query.filter_by(first_name=auth.username).first()

        if instance.password == auth.password:
            try:
                token = Token(user_id=instance.id)
                db.session.add(token)
                db.session.commit()
                db.session.flush()
                db.session.refresh(token)
            except IntegrityError:
                db.session.rollback()
                token = Token.query.filter_by(user_id=instance.id).first()
            return {"token": token.key}

        return {"message": "Some Error"}
