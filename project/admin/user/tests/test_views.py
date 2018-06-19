# !/usr/bin/python
# -*- coding: utf-8 -*-
""" Created by andresilva on 2/22/16"""
from flask import url_for
from project.tests.base import MVCTestCase
import project.user.models as umodels


class UserAdminViewsTestCase(MVCTestCase):

    def setUp(self):
        super(UserAdminViewsTestCase, self).setUp()
        self.me = self.create_user(username="abcdef", password="abcdef",
                                   is_admin=True)
        # login to access admin pages
        data = dict(username="abcdef", password="abcdef")
        self.client.post(url_for("user.login"), data=data,
                         follow_redirects=True)

    def test_user_create_loads(self):
        # Ensure user create admin page loads as expected
        res = self.client.get(url_for("admin.user_create"),
                              follow_redirects=True)
        self.assertEqual(res.status_code, 200)
        # test: create user with complete form data
        data = dict(username="myusername", password="mypassword",
                    email="myusername@test.com")
        res = self.client.post(url_for("admin.user_create"), data=data,
                               follow_redirects=True)
        user = umodels.User.objects.filter(username="myusername").first()
        url = url_for("admin.user_detail", user_id=str(user))
        msg = ("<span>User user <a href=\"{}\">{}</a> was successfully "
               "created.</span>".format(url, str(user)))
        self.assertIn(msg, res.data)
        # test: try to create user with existing username and email
        data = dict(username="myusername", password="mypassword",
                    email="myusername@test.com")
        res = self.client.post(url_for("admin.user_create"), data=data,
                               follow_redirects=True)
        self.assertIn(b'Username &#34;myusername&#34; already exists.',
                      res.data)
        self.assertIn(b'Email &#34;myusername@test.com&#34; already exists.',
                      res.data)
        # test: create non admin user
        self.assertFalse(user.is_admin)
        # test: create admin user
        data = dict(username="admin", password="adminpassword",
                    email="admin@test.com", is_admin=True)
        self.client.post(url_for("admin.user_create"), data=data,
                               follow_redirects=True)
        user = umodels.User.objects.filter(username="admin").first()
        self.assertTrue(user.is_admin)

    def test_user_detail_view(self):
        """Ensure user detail page is loading"""
        res = self.client.get(url_for("admin.user_detail",
                                      user_id=str(self.me)),
                              follow_redirects=True)
        self.assertEqual(res.status_code, 200)
        # test: invalid user id
        res = self.client.get(url_for("admin.user_detail", user_id="_id"),
                              follow_redirects=True)
        self.assertEqual(res.status_code, 404)

    def test_user_toggle_view(self):
        """Ensure view user_toggle is changing values correctly"""
        # test: toggle id_admin flag
        self.assertTrue(self.me.is_admin)
        res = self.client.get(
            url_for("admin.user_toggle", user_id=str(self.me),
                    action="is_admin"),
            follow_redirects=True)
        self.me.reload()
        msg = ("User \"{}\" field \"{}\" was successfully updated to \"{}\"!"
               "".format(str(self.me), "is_admin", self.me.is_admin))
        self.assertIn(msg, res.data)
        self.assertFalse(self.me.is_admin)
        self.me.is_admin = not self.me.is_admin
        self.me.save()
        # test: remove user
        res = self.client.get(
            url_for("admin.user_toggle", user_id=str(self.me),
                    action="remove"), follow_redirects=True)
        self.me.reload()
        msg = "User \"{}\" was successfully deleted!".format(str(self.me))
        self.assertIn(msg, res.data)
        self.assertEqual(0, umodels.User.objects.count())
        self.assertEqual(1, umodels.User._objects.count())
        self.assertEqual(self.me, umodels.User._objects.first())
        self.me._is_deleted = not self.me._is_deleted
        self.me.save()
        # test: invalid user_id
        res = self.client.get(
            url_for("admin.user_toggle", user_id=str("_id"), action="?"),
            follow_redirects=True)
        msg = "User with id \"{}\" does not exist.".format("_id")
        self.assertIn(msg, res.data)
