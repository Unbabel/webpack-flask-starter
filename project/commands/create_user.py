# !/usr/bin/python
# -*- coding: utf-8 -*-
"""Created by andresilva on 6/15/16"""
from flask import current_app as app
from flask_script import Command, Option
from project.user.models import User


class CreateUserCommand(Command):
    """Creates user by giving username and password"""

    def __init__(self):
        super(CreateUserCommand, self).__init__()
        self.username = None
        self.password = None
        self.is_admin = False

    def get_options(self):
        return [
            Option('-u', '--username', dest='username', default=self.username),
            Option('-p', '--password', dest='password', default=self.password),
            Option('--is_admin', dest='is_admin', action="store_true",
                   default=self.is_admin)
        ]

    def run(self, **kwargs):
        app.logger.info("Running {} with arguments {}".format(
            self.__class__.__name__, kwargs))
        self.__dict__.update(**kwargs)  # update self's with kwargs
        try:
            user = User.create(self.username, self.password,
                               is_admin=self.is_admin)
            user.save()
            app.logger.info("User \"{}\" was successfully created!".format(
                self.username))
        except Exception as e:
            app.logger.error("Something went wrong :s. {}".format(e))
