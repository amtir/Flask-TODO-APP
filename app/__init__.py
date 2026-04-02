from flask import Flask

from app.routes.todos import bp as todos_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(todos_bp)
    return app
