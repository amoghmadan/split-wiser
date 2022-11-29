from flask import Blueprint

from routes.api.v1.expense import expense
from routes.api.v1.friends import friends
from routes.api.v1.groups import groups
from routes.api.v1.group_friends import group_friends
from routes.api.v1.tokens import tokens
from routes.api.v1.users import users

routes = [
    ("/expenses", expense),
    ("/friends", friends),
    ("/groups", groups),
    ("/group-friends", group_friends),
    ("/login", tokens),
    ("/users", users),

]

v1 = Blueprint("v1", __name__)
for prefix, route in routes:
    v1.register_blueprint(route, url_prefix=prefix)

__all__ = ["v1"]
