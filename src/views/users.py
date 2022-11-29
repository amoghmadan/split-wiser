from http import HTTPStatus

from flask import jsonify, request, views
from marshmallow.validate import ValidationError

from models import Token, User
from schemas import LoginSchema, UserSchema
from utilities import db, viewsets


class RegisterUserView(viewsets.ModelViewSet):
    """User: View Set"""

    model = User
    schema_class = UserSchema


class LoginUserView(views.MethodView):
    schema_class = LoginSchema

    def post(self):
        try:
            payload = self.schema_class(request.json)
        except ValidationError as e:
            return jsonify(e.messages), HTTPStatus.BAD_REQUEST
        user = User.query.filter_by(email=payload["email"]).first()
        if not user:
            pass
        if not user.check_password(payload["password"]):
            pass
        token = Token.query.filter_by(user_id=user.id).first()
        if not token:
            token = Token(user_id=user.id)
            db.session.add(token)
            db.session.commit()
            db.reflect(token)
        return jsonify({"token": token.key}), HTTPStatus.CREATED
