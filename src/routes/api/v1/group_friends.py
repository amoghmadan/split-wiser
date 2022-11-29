from flask import Blueprint

from views import GroupFriendViewSet

group_friends = Blueprint("group_friends", __name__)
group_friends.add_url_rule(
    "/", view_func=GroupFriendViewSet.as_view("group-list"), methods=["GET", "POST"]
)
group_friends.add_url_rule(
    "/<id>",
    view_func=GroupFriendViewSet.as_view("group-detail"),
    methods=["GET", "PUT", "PATCH", "DELETE"]
)
