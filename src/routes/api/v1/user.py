from flask import Blueprint

from views import UserViewSet

user = Blueprint("user", __name__)
user.add_url_rule(
    "/", view_func=UserViewSet.as_view("user-list"), methods=["GET", "POST"]
)
user.add_url_rule(
    "/<id>",
    view_func=UserViewSet.as_view("user-detail"),
    methods=["GET", "PUT", "PATCH", "DELETE"]
)