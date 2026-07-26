from flask import Flask

from app.routes.pages import pages_bp
from app.routes.terminal import terminal_bp


def create_app():

    app = Flask(__name__)

    app.secret_key = "portfolio-os-development-key"

    app.register_blueprint(pages_bp)

    app.register_blueprint(
        terminal_bp,
        url_prefix="/api"
    )

    return app