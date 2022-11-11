from flask import Flask

import settings


def get_application():
    app = Flask(__name__)
    return app


application = get_application()

if __name__ == "__main__":
    application.run(debug=settings.DEBUG)
