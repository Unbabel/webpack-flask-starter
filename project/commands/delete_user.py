# !/usr/bin/python
# -*- coding: utf-8 -*-
"""Created by andresilva on 6/15/16"""
from flask import current_app as app
from flask_script import Command, Option
from project.user.models import User


class DeleteUserCommand(Command):
    """Deletes user by giving username"""

    def __init__(self):
        super(DeleteUserCommand, self).__init__()
        self.username = None

    def get_options(self):
        return [
            Option('-u', '--username', dest='username', default=self.username),
        ]

    def run(self, **kwargs):
        app.logger.info("Running {} with arguments {}".format(
            self.__class__.__name__, kwargs))
        self.__dict__.update(**kwargs)  # update self's with kwargs
        try:
            user = User._objects.get(username=self.username)
            user.delete(force=True)
            user.save()
            app.logger.info("User \"{}\" was successfully deleted!".format(
                self.username))
        except Exception as e:
            app.logger.error("Something went wrong :s. {}".format(e))
