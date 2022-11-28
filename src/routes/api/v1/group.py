from flask import Blueprint

from views import GroupViewSet

group = Blueprint("user", __name__)
group.add_url_rule(
    "/", view_func=GroupViewSet.as_view("group-list"), methods=["GET", "POST"]
)
group.add_url_rule(
    "/<id>",
    view_func=GroupViewSet.as_view("group-detail"),
    methods=["GET", "PUT", "PATCH", "DELETE"]
)
