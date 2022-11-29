from flask import Blueprint

from views import GroupViewSet

groups = Blueprint("groups", __name__)
groups.add_url_rule(
    "/", view_func=GroupViewSet.as_view("group-list"), methods=["GET", "POST"]
)
groups.add_url_rule(
    "/<id>",
    view_func=GroupViewSet.as_view("group-detail"),
    methods=["GET", "PUT", "PATCH", "DELETE"]
)
