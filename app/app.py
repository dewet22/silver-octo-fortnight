# -*- coding: utf-8 -*-

from flask import Flask, Config


def create_app(config_object: Config):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    import app.extensions as ext
    ext.db.init_app(app)
