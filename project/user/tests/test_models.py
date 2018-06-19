# !/usr/bin/python
# -*- coding: utf-8 -*-
""" Created by andresilva on 2/22/16"""
from mongoengine import ValidationError
from flask_bcrypt import check_password_hash
from flask_login import current_user, login_user
from project.tests.base import MVCTestCase
import project.user.models as umodels


class UserModelTestCase(MVCTestCase):

    def setUp(self):
        super(UserModelTestCase, self).setUp()
        self.user = self.create_user(username="username", password="password")

    def test_user_representation(self):
        """Ensure user object __repr__, __str__ are returning correct values"""
        self.assertEqual(str(self.user), self.user.username)
        self.assertEqual(repr(self.user), "<User: {}>".format(str(self.user)))

    def test_user_creation_method_and_model_fields(self):
        """Ensure when creating a User Object that the method used to create
        the user assigns all fields correctly"""
        user = umodels.User.create(username="my_username",
                                   password="my_password")
        self.assertEqual(user.username, "my_username")
        self.assertTrue(check_password_hash(user.password, "my_password"))

    def test_get_user(self):
        """Ensure get_user classmethod is returning always what we expect"""
        # test: invalid input
        self.assertRaises(ValidationError, umodels.User.get_user, None)
        # test: UserMixin (from flask.login) object
        self.assertEqual(self.user, umodels.User.get_user(self.user))
        # test: LocalProxy object
        login_user(self.user)
        self.assertEqual(self.user, umodels.User.get_user(current_user))
        # test: User Object from db but by "username" and by "id"
        self.assertEqual(self.user, umodels.User.get_user("username"))
        self.assertEqual(self.user, umodels.User.get_user(self.user.id))

    def test_reset_password(self):
        """Ensure the reset password method is actually updating the password
        to the given one"""
        self.assertTrue(check_password_hash(self.user.password, "password"))
        self.user.reset_password("newpassword")
        self.user.save()
        self.user.reload()
        self.assertFalse(check_password_hash(self.user.password, "password"))
        self.assertTrue(check_password_hash(self.user.password, "newpassword"))

    def test_delete_user(self):
        """Ensure delete method is not actually deleting the editor, but only
        deletes it from the database if the flag "force" is given"""
        self.assertEqual(1, umodels.User.objects.count())
        self.user.delete()
        self.assertEqual(0, umodels.User.objects.count())
        self.assertEqual(1, umodels.User._objects.count())
        self.user.delete(force=True)
        self.assertEqual(0, umodels.User.objects.count())
        self.assertEqual(0, umodels.User._objects.count())
