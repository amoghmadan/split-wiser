from flask import Blueprint

from views import TokenViewSet

token = Blueprint("token", __name__)
token.add_url_rule(
    "/", view_func=TokenViewSet.as_view("token-list"), methods=["GET", "POST"]
)