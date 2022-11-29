from flask import Blueprint

from views import TokenViewSet

tokens = Blueprint("tokens", __name__)
tokens.add_url_rule(
    "/", view_func=TokenViewSet.as_view("token-list"), methods=["GET", "POST"]
)
