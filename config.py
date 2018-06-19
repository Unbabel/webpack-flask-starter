# !/usr/bin/python
# -*- coding: utf-8 -*-
""" Created by andresilva on 2/19/16"""
import os


class BaseConfig(object):
    DEBUG = False
    TESTING = True
    MACHINE_NAME = "Flask Template Project"
    SECRET_KEY = os.environ.get("SECRET_KEY")
    MONGODB_DB = os.environ.get("MONGO_DB", "default")

    # Third party services
    # codacy.com
    # Coverage given by codacy.com. You need to register you project
    # there so they can give you the access token for this functionality
    CODACY_PROJECT_TOKEN = os.environ.get("CODACY_PROJECT_TOKEN")


class TestConfig(BaseConfig):
    DEBUG = True
    WTF_CSRF_ENABLED = False
    DEBUG_TB_PROFILER_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    MONGODB_DB = os.environ.get("MONGO_DB_TEST", "default_test")


class LocalhostConfig(BaseConfig):
    DEBUG = True
    DEBUG_TB_PROFILER_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    # TODO not working because current version of DebugToolbar doesn't allow this.
    DEBUG_TB_PANELS = (
        'flask_debugtoolbar.panels.versions.VersionDebugPanel',
        'flask_debugtoolbar.panels.timer.TimerDebugPanel',
        'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
        'flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
        'flask_debugtoolbar.panels.config_vars.ConfigVarsDebugPanel',
        'flask_debugtoolbar.panels.template.TemplateDebugPanel',
        'flask_debugtoolbar.panels.sqlalchemy.SQLAlchemyDebugPanel',
        'flask_debugtoolbar.panels.logger.LoggingPanel',
        'flask_debugtoolbar.panels.route_list.RouteListDebugPanel',
        'flask_debugtoolbar.panels.profiler.ProfilerDebugPanel',
        'flask_mongoengine.panels.MongoDebugPanel',
    )


class StagingConfig(BaseConfig):
    DEBUG = True
    TESTING = False
    DEBUG_TB_PROFILER_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False


config = {
    '_baseconfig': BaseConfig,
    'localhost': LocalhostConfig,
    'test': TestConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}

__all__ = ['config']
