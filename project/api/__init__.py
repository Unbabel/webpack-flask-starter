# !/usr/bin/python
# -*- coding: utf-8 -*-
"""Created by andresilva on 12/31/16"""
from flask_restful import Resource
from .version import Version

API_VERSION = "/api/v1{}"


class Home(Resource):
    """Home directory for API v1. See all available endoints"""

    @staticmethod
    def get():
        """Shows scheme of API"""
        return dict((API_VERSION.format(endpoint), resource.__doc__)
                    for resource, endpoint in Resources), 200


Resources = [
    # (<endpoint url>, <resource model>)
    (Home, "/"),
    (Version, "/version/"),
]


__author__ = "andresilva"
__email__ = "andre@unbabel.com"
__all__ = ["Resources"]
