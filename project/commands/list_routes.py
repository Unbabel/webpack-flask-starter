# !/usr/bin/python
# -*- coding: utf-8 -*-
"""Created by andresilva on 6/15/16"""
import urllib.parse
from flask import url_for, current_app as app

from flask_script import Command


class ListRoutesCommand(Command):
    """List of routes"""

    def run(self):
        app.logger.info("Running {}".format(self.__class__.__name__))

        output = []
        for rule in app.url_map.iter_rules():
            options = {}
            for arg in rule.arguments:
                options[arg] = "[{0}]".format(arg)

            methods = ','.join(rule.methods)
            url = url_for(rule.endpoint, **options)
            line = urllib.parse.unquote("{:50s} {:20s} {}".format(
                rule.endpoint, methods, url))
            output.append(line)

        for line in sorted(output):
            print(line)
