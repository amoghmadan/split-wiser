from flask import Blueprint

from views import FriendViewSet

friends = Blueprint("friends", __name__)
friends.add_url_rule(
    "/", view_func=FriendViewSet.as_view("friend-list"), methods=["GET", "POST"]
)
friends.add_url_rule(
    "/<id>",
    view_func=FriendViewSet.as_view("friend-detail"),
    methods=["GET", "PUT", "PATCH", "DELETE"]
)
