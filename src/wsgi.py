from flask import Flask

from routes import routes
from utilities import db, ma, migrate
import settings


def get_application():
    """Get application"""
    app = Flask(__name__)
    app.config.update(
        DEBUG=settings.DEBUG,
        ENV=settings.ENV,
        SQLALCHEMY_DATABASE_URI=settings.SQLALCHEMY_DATABASE_URI,
        SQLALCHEMY_TRACK_MODIFICATIONS=settings.SQLALCHEMY_TRACK_MODIFICATIONS,
    )
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    for prefix, route in routes:
        app.register_blueprint(route, url_prefix=prefix)
    return app


application = get_application()

if __name__ == "__main__":
    """Run application (development)"""
    application.run()
