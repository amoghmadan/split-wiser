from functools import wraps
from http import HTTPStatus

from flask import request, jsonify

from models import Token


class TokenAuthentication:
    """Token Authentication"""

    header = "Authorization"
    keyword = "Bearer"
    model = Token

    def __call__(self, get_response):
        """Decorator"""
        response = {"detail": "Unauthorized"}

        @wraps(get_response)
        def authenticate(*args, **kwargs):
            authorization = request.headers.get(self.header)
            if authorization is None:
                return jsonify(response), HTTPStatus.UNAUTHORIZED
            try:
                keyword, token = authorization.split()
            except ValueError:
                return jsonify(response), HTTPStatus.UNAUTHORIZED
            if self.keyword.lower() != keyword.lower():
                return jsonify(response), HTTPStatus.UNAUTHORIZED
            token = self.model.query.filter_by(key=token).first()
            if token is None:
                return jsonify(response), HTTPStatus.UNAUTHORIZED
            kwargs["user"] = token.user
            return get_response(*args, **kwargs)
        return authenticate
