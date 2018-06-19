# !/usr/bin/python
# -*- coding: utf-8 -*-
""" Created by andresilva on 2/22/16"""
from flask import url_for
from project.tests.base import MVCTestCase


class UserViewsTestCase(MVCTestCase):

    def setUp(self):
        super(UserViewsTestCase, self).setUp()

    def test_login_page_loads(self):
        # Ensure login page loads as expected
        res = self.client.get(url_for("user.login"),
                               follow_redirects=True)
        self.assertIn(b'Please login', res.data)
        self.assertEqual(res.status_code, 200)
        # test: with invalid credentials
        data = dict(username="username", password="password")
        res = self.client.post(url_for("user.login"), data=data,
                               follow_redirects=True)
        self.assertIn(b'Invalid Credentials. Please try again.', res.data)

    def test_settings_page_loads(self):
        # Ensure settings page loads as expected
        self.create_user()
        data = dict(username="username", password="password")
        res = self.client.post(url_for("user.login"), data=data,
                               follow_redirects=True)
        self.assertIn(b'Welcome username.', res.data)
        res = self.client.get(url_for("user.settings"),
                               follow_redirects=True)
        self.assertIn(b'Welcome to your dashboard username.', res.data)
        self.assertEqual(res.status_code, 200)

    def test_register_page(self):
        """Ensure sign in is working properly"""
        # test: get request loads page correctly
        res = self.client.get(url_for("user.register"),
                              follow_redirects=True)
        self.assertEqual(res.status_code, 200)
        # test: post request, creates new user with the following data
        data = dict(username="myusername", password="mypassword",
                    confirm_password="mypassword")
        res = self.client.post(url_for("user.register"), data=data,
                               follow_redirects=True)
        self.assertIn(b'Welcome myusername.', res.data)
        # test: try to register same username
        data = dict(username="myusername", password="mypassword",
                    confirm_password="mypassword")
        res = self.client.post(url_for("user.register"), data=data,
                               follow_redirects=True)
        self.assertIn(b'Username &#34;myusername&#34; already exists.',
                      res.data)

    def test_logout(self):
        # Ensure logout behaves correctly
        self.create_user(username="username", password="password")
        data = dict(username="username", password="password")
        res = self.client.post(url_for("user.login"), data=data,
                         follow_redirects=True)
        self.assertIn(b'Welcome username.', res.data)
        res = self.client.get(url_for("user.logout"), follow_redirects=True)
        self.assertIn(b'You were logged out.', res.data)
