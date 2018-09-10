# !/usr/bin/python
# -*- coding: utf-8 -*-
""" Created by andresilva on 2/19/16"""
import os
from flask import Flask


def read_env(app, config_class):
    """config environment variables
    use configuration given by environment variable APP_ENV if "config_class"
    is not given"""
    # get correct APP_ENV and right variable
    if config_class is None:
        from config import config as c
        config_class = c.get(app.config.get('APP_ENV'))
    app.config.from_object(config_class)
    return app


def create_app(config=None):
    app = Flask(__name__)
    # read .envs and configuration class
    app = read_env(app, config)

    # define logging patterns
    import logging  # %(pathname)
    if app.config.get("TESTING"):
        log_format = ("[%(asctime)s] %(funcName)s:%(lineno)d "
                      "%(levelname)s - %(message)s")
        log_level = logging.DEBUG

    else:
        log_format = ("[%(asctime)s] {%(filename)s#%(funcName)s:%(lineno)d} "
                      "%(levelname)s - %(message)s")
        log_level = logging.INFO

    formatter = logging.Formatter(log_format)
    handler = logging.StreamHandler()
    handler.setLevel(log_level)
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.logger.setLevel(log_level)
    # remove default Flask debug handler
    del app.logger.handlers[0]

    # setup apps
    from flask_debugtoolbar import DebugToolbarExtension
    from flask_mongoengine import MongoEngine
    from flask_bcrypt import Bcrypt
    from flask_rq2 import RQ
    from flask_restful import Api
    from flask_login import LoginManager

    DebugToolbarExtension(app)
    MongoEngine(app)
    Bcrypt(app)
    RQ(app)
    api = Api(app)
    login_manager = LoginManager(app)

    # register view blueprints
    from project.home.views import app_blueprint
    from project.admin.views import admin_blueprint
    from project.user.views import user_blueprint

    app.register_blueprint(app_blueprint)
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(user_blueprint)

    # register api endpoints
    from .api import Resources, API_VERSION
    for resource, url in Resources:
        _endpoint = ".".join(API_VERSION.format(url).split("/")[1:-1])
        api.add_resource(resource, API_VERSION.format(url), endpoint=_endpoint)

    # import custom login manager functions
    from project.home.login_manager import load_user_from_request, load_user
    login_manager.login_view = "user.login"
    login_manager.user_loader(load_user)
    login_manager.request_loader(load_user_from_request)

    # jinja extensions
    app.jinja_env.add_extension('jinja2.ext.do')

    # default flashed messages category
    login_manager.login_message_category = 'info'
    login_manager.needs_refresh_message_category = 'info'

    return app

__version_info__ = ('1', '0', '0')
__author__ = "andresilva"
__email__ = "andre@unbabel.com"
