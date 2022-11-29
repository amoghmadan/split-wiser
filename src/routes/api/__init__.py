from flask import Blueprint

from routes.api.v1 import v1

routes = [
    ("/v1", v1),
]

api = Blueprint("api", __name__)
for prefix, route in routes:
    api.register_blueprint(route, url_prefix=prefix)

__all__ = ["api"]
