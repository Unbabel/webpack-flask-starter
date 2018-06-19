# !/usr/bin/python
# -*- coding: utf-8 -*-
""" Created by andresilva on 2/22/16"""
from flask import url_for
from project.tests.base import MVCTestCase


class HomeViewsTestCase(MVCTestCase):

    def setUp(self):
        super(HomeViewsTestCase, self).setUp()

    def test_home_page_loads(self):
        # Ensure home view loads properlly
        res = self.client.get(url_for("app.home"), follow_redirects=True)
        self.assertEqual(res.status_code, 200)