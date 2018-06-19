# !/usr/bin/python
# -*- coding: utf-8 -*-
"""Created by andresilva on 7/8/16"""
from flask import current_app as app
from flask_login import current_user
from functools import wraps


def admin_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not current_user.is_admin:
            return app.login_manager.unauthorized()
        return func(*args, **kwargs)
    return decorated_view
