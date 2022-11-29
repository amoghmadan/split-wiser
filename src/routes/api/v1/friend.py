from flask import Blueprint

from views import FriendViewSet

friend = Blueprint("friend", __name__)
friend.add_url_rule(
    "/", view_func=FriendViewSet.as_view("friend-list"), methods=["GET", "POST"]
)
friend.add_url_rule(
    "/<id>",
    view_func=FriendViewSet.as_view("friend-detail"),
    methods=["GET", "PUT", "PATCH", "DELETE"]
)
