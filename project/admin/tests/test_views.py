# !/usr/bin/python
# -*- coding: utf-8 -*-
""" Created by andresilva on 2/22/16"""
from flask import url_for
from project.tests.base import MVCTestCase


class AdminViewsTestCase(MVCTestCase):

    def setUp(self):
        super(AdminViewsTestCase, self).setUp()
        self.me = self.create_user(username="abcdef", password="abcdef",
                                   is_admin=True)
        # login to access admin pages
        data = dict(username="abcdef", password="abcdef")
        self.client.post(url_for("user.login"), data=data,
                         follow_redirects=True)

    def test_home_view_redirects(self):
        # Ensure all redirects from admin.home are working fine
        res = self.client.get(url_for("admin.home_users"),
                              follow_redirects=True)
        self.assertEqual(res.status_code, 200)
