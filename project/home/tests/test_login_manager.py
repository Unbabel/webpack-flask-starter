# !/usr/bin/python
# -*- coding: utf-8 -*-
"""Created by andresilva on 7/8/16"""

from project.tests.base import UtilsTestCase
import base64
import project.home.login_manager as lm


class LoginManagerUtilsTestCase(UtilsTestCase):

    def setUp(self):
        super(LoginManagerUtilsTestCase, self).setUp()
        self.user = self.create_user(is_admin=True)

    def test_load_user(self):
        """Ensure load_user method is properly working"""
        # test: invalid user id arguments
        self.assertFalse(lm.load_user(None))
        self.assertFalse(lm.load_user("None"))
        self.assertFalse(lm.load_user(""))
        self.assertFalse(lm.load_user("?"))
        # test: valid user id
        self.assertEqual(self.user, lm.load_user(self.user.id))

    def test_load_user_from_request(self):
        """Ensure load_user_from_request is working fine either for
        authentication by api_key and Basic"""
        # test: invalid arguments
        reqctx = self.app.test_request_context("?", headers=[])
        self.assertIsNone(lm.load_user_from_request(reqctx.request))
        # test: invalid api key
        reqctx = self.app.test_request_context("?api_key=1234")
        self.assertIsNone(lm.load_user_from_request(reqctx.request))
        # test: valid api key
        reqctx = self.app.test_request_context(
            "?api_key={}".format(self.user.api_key))
        response = lm.load_user_from_request(reqctx.request)
        self.assertIsNotNone(response)
        self.assertEqual(response, self.user)
        # test: invalid auth Basic String
        reqctx = self.app.test_request_context(
            headers={'Authorization': b"lol?"})
        self.assertIsNone(lm.load_user_from_request(reqctx.request))
        # test: valid auth Basic but invalid base64 user:password
        reqctx = self.app.test_request_context(
            headers={'Authorization': b"Basic lol?"})
        self.assertIsNone(lm.load_user_from_request(reqctx.request))
        # test: valid auth Basic and valid base64 api_key
        api_key = base64.b64encode(bytes(self.user.api_key, 'utf8'))
        reqctx = self.app.test_request_context(
            headers={'Authorization': b"Basic " + api_key})
        response = lm.load_user_from_request(reqctx.request)
        self.assertIsNotNone(response)
        self.assertEqual(response, self.user)
        # test: valid auth Basic and valid base64 userpassword
        userpass = base64.b64encode(b"username:password")
        reqctx = self.app.test_request_context(
            headers={'Authorization': b"Basic " + userpass})
        response = lm.load_user_from_request(reqctx.request)
        self.assertIsNotNone(response)
        self.assertEqual(response, self.user)
