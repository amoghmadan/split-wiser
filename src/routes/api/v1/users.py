from flask import Blueprint

from views import RegisterUserView

users = Blueprint("users", __name__)
users.add_url_rule(
    "/", view_func=RegisterUserView.as_view("user-list"), methods=["POST"]
)
