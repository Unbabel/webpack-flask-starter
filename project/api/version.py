# !/usr/bin/python
# -*- coding: utf-8 -*-
"""Created by andresilva on 12/31/16"""
from flask import current_app as app
from flask_restful import reqparse, Resource


parser = reqparse.RequestParser()


class Version(Resource):
    """Version of API"""

    @staticmethod
    def get():
        """Shows version of app """
        from manage import __version__
        return {
            "status": 200,
            "version": __version__,
            "name": app.config.get('MACHINE_NAME')
        }, 200
