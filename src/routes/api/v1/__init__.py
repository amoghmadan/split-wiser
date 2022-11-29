from flask import Blueprint

from routes.api.v1.friend import friend
from routes.api.v1.user import user
from routes.api.v1.group import group

routes = [
    ("/friends", friend),
    ("/users", user),
    ("/groups", group)
]

v1 = Blueprint("v1", __name__)
for prefix, route in routes:
    v1.register_blueprint(route, url_prefix=prefix)

__all__ = ["v1"]
