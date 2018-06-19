# !/usr/bin/python
# -*- coding: utf-8 -*-
""" Created by andresilva on 2/22/16"""
import project.user.models as umodels


class UserTestUtils(object):

    def setUp(self):
        """"""
        super(UserTestUtils, self).setUp()

    @staticmethod
    def create_user(username=None, password=None, is_admin=False):
        """Aux test method that creates user from given arguments"""
        if username is None:
            username = "username"
        if password is None:
            password = "password"

        kwargs = dict([
            ("username", username),
            ("password", password),
            ("is_admin", is_admin)
        ])
        return umodels.User.create(**kwargs)
