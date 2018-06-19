# !/usr/bin/python
# -*- coding: utf-8 -*-
"""Created by andresilva on 6/11/16"""
from flask import flash as FLASH
from bs4 import BeautifulSoup


ALERT_LINK_CLASS = ['alert-link']


def flash(message, category='default'):
    """For the given message, if html is present, add bootstrap .alert-link
    class to all links"""
    if message.startswith('<p>') and message.endswith('</p>'):
        message = BeautifulSoup(message, "lxml")
        for a in message.find_all("a"):
            if not a.get('class'):
                a.attrs.update({'class': []})
            a['class'].extend(ALERT_LINK_CLASS)
        message = str(message)

    FLASH(message, category)


def danger(message):
    flash(message, category="danger")


def warning(message):
    flash(message, category="warning")


def info(message):
    flash(message, category="info")


def success(message):
    flash(message, category="success")


__all__ = ['success', 'info', 'warning', 'danger']
