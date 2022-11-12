from flask import Blueprint

routes = []

v1 = Blueprint("v1", __name__)
for prefix, route in routes:
    v1.register_blueprint(route, url_prefix=prefix)

__all__ = ["v1"]
