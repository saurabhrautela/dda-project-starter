from flask import Flask
from . import db, note


def create_app():
    app = Flask(__name__)

    db.init_app(app)

    app.register_blueprint(note.bp)

    return app
