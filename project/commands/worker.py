# !/usr/bin/python
# -*- coding: utf-8 -*-
"""Created by andresilva on 6/15/16"""

from flask import current_app as app
from flask_script import Command
from flask_rq2 import RQ


class WorkerCommand(Command):
    """runs Worker instance"""

    def __init__(self):
        super(WorkerCommand, self).__init__()
        self.rq = RQ()

    def run(self, **kwargs):
        app.logger.info("Running {} with arguments {}".format(
            self.__class__.__name__, kwargs))
        self.__dict__.update(**kwargs)  # update self's with kwargs
        self.rq.get_worker().work()
