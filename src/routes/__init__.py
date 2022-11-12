from flask import Blueprint

from routes.api import api

routes = [
    ("/api", api),
]
