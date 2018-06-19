# !/usr/bin/python
# -*- coding: utf-8 -*-
""" Created by andresilva on 2/22/16"""
from project import create_app
from flask_testing import TestCase
import project.tests.utils as tu


class BaseTestCase(tu.UserTestUtils, TestCase):
    """BaseTestCase"""
    @classmethod
    def setUpClass(cls):
        """Make sure correct database is being used and if so, that is clean"""
        super(BaseTestCase, cls).setUpClass()
        cls.app = create_app("config.TestConfig")
        cls.app.logger.info("Using \"{}\" database".format(
            cls.app.config.get('MONGODB_DB')))
        # QUESTION: should we clean the database here?

    def create_app(self):
        return self.app

    def setUp(self):
        """Init Database values for testing"""
        self.app.logger.info("========== SETUP ==========")
        super(BaseTestCase, self).setUp()
        self.app.logger.info("========== END OF SETUP ==========")

    def tearDown(self):
        """Remove Database values """
        from mongoengine import connection
        conn = connection.get_connection()
        conn.drop_database(self.app.config.get('MONGODB_DB'))
        super(BaseTestCase, self).tearDown()


class MVCTestCase(BaseTestCase):
    """Default base test case for every
    <Model|View|Controller(Form)>TestCase"""
    pass


class UtilsTestCase(BaseTestCase):
    """Default utils test case for every utils/<file>.py"""
    pass
