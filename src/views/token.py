import binascii
import os
from flask import views, request

from models import Token, User
from utilities import db


class TokenViewSet(views.MethodView):

    def generate_key(self):
        """It will generate the token"""
        return binascii.hexlify(os.urandom(20)).decode()

    def get(self, *args, **kwargs):
        # breakpoint()
        auth = request.authorization
        if not auth or not auth.username or not auth.password:
            return {"message": "could not verify"}

        instance = User.query.filter_by(first_name=auth.username).first()

        if instance.password == auth.password:
            token = self.generate_key()
            data = Token(user_id=instance.id, key=token)
            db.session.add(data)
            db.session.commit()
            return {"token": token}

        return {"message": "Some Error"}
