from flask import Blueprint

from views import UserViewSet

users = Blueprint("users", __name__)
users.add_url_rule(
    "/", view_func=UserViewSet.as_view("user-list"), methods=["GET", "POST"]
)
users.add_url_rule(
    "/<id>",
    view_func=UserViewSet.as_view("user-detail"),
    methods=["GET", "PUT", "PATCH", "DELETE"]
)