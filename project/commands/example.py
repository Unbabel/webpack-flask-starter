# !/usr/bin/python
# -*- coding: utf-8 -*-
"""Created by andresilva on 6/15/16"""

from flask import current_app as app

from flask_script import Command, Option


class HelloCommand(Command):

    def __init__(self):
        super(HelloCommand, self).__init__()
        self.name = "joe"

    def get_options(self):
        return [
            Option('-n', '--name', dest='name', default=self.name),
        ]

    def run(self, **kwargs):
        app.logger.info("Running {} with arguments {}".format(
            self.__class__.__name__, kwargs))
        self.__dict__.update(**kwargs)  # update self's with kwargs
        print("hello", self.name)
