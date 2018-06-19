# !/usr/bin/python
# -*- coding: utf-8 -*-
""" Created by andresilva on 2/22/16"""
from flask import get_flashed_messages

from project.tests.base import UtilsTestCase
from project.utils.flash import (flash, success, warning, info, danger,
                                 ALERT_LINK_CLASS)


class FlashUtilsTestCase(UtilsTestCase):

    def assert_flashes(self, expected_message, expected_category='message'):
        flashed_messages = get_flashed_messages(with_categories=True)
        for category, message in flashed_messages:
            if category == expected_category:
                self.assertEqual(message, expected_message)
                return
        raise AssertionError("nothing flashed")

    def setUp(self):
        super(FlashUtilsTestCase, self).setUp()
        self.simple_message = "This is a simpple flash message"
        self.html_message = (
            '<p><a>This is <b>html</b> <strong>flash</strong>message</a></p>'
        )
        self.html_w_a_class_message = (
            '<html><body><p><a class="{}">This is <b>html</b> <strong>flash'
            '</strong>message</a></p></body></html>'
            ''.format(ALERT_LINK_CLASS[0])
        )

    def test_flash_different_categories(self):
        """Ensure all 4 categories work properly"""
        success(self.simple_message)
        warning(self.simple_message)
        info(self.simple_message)
        danger(self.simple_message)
        self.assert_flashes(self.simple_message, 'success')
        self.assert_flashes(self.simple_message, 'warning')
        self.assert_flashes(self.simple_message, 'info')
        self.assert_flashes(self.simple_message, 'danger')

    def test_flash_behaviour_with_html(self):
        """Ensure default flash works with html input"""
        flash(self.html_message)
        self.assert_flashes(self.html_w_a_class_message, 'default')

        flash(self.html_w_a_class_message)
        self.assert_flashes(self.html_w_a_class_message, 'default')
