from flask import Blueprint

from routes.api.v1.friend import friend
from routes.api.v1.users import users
from routes.api.v1.group import group
from routes.api.v1.token import token

routes = [
    ("/friends", friend),
    ("/users", users),
    ("/groups", group),
    ("/token", token)
]

v1 = Blueprint("v1", __name__)
for prefix, route in routes:
    v1.register_blueprint(route, url_prefix=prefix)

__all__ = ["v1"]
