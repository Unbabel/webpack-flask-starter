# !/usr/bin/python
# -*- coding: utf-8 -*-
"""Created by andresilva on 6/15/16"""

import unittest

from flask import current_app as app
from flask_script import Command, Option


class TestCommand(Command):
    """runs tests"""

    def __init__(self):
        super(TestCommand, self).__init__()
        self.folder = "project/"
        self.pattern = "test*.py"
        self.test_name = None

    def get_options(self):
        return [
            Option('-f', '--folder', dest='folder', default=self.folder),
            Option('-p', '--pattern', dest='pattern', default=self.pattern),
            Option('-n', '--name', dest='test_name', default=self.test_name),
        ]

    def run(self, **kwargs):
        app.logger.info("Running {} with arguments {}".format(
            self.__class__.__name__, kwargs))
        self.__dict__.update(**kwargs)  # update self's with kwargs
        if self.test_name is None:
            tests = unittest.TestLoader().discover(start_dir=self.folder,
                                                   pattern=self.pattern)
        else:
            tests = unittest.TestLoader().loadTestsFromName(self.test_name)
        unittest.TextTestRunner(verbosity=2).run(tests)
