# !/usr/bin/python
# -*- coding: utf-8 -*-
""" Created by andresilva on 2/19/16"""
from flask import redirect, render_template, request, Blueprint
from flask_login import login_required, logout_user, current_user
from flask_mongoengine import Pagination

from project.home.decorators import admin_required
from project.api import Resources

admin_blueprint = Blueprint('admin', __name__)


@admin_blueprint.route('/admin/users/')
def home_users():
    return redirect("/admin/#users")


@admin_blueprint.route('/admin/')
@login_required
@admin_required
def home():
    params = request.args.to_dict()

    # user pagination
    upage = int(params.get('user-page', 1))
    users = Pagination(umodels.User.objects.all(), upage, 20)

    return render_template('admin/home.html', **{
        'users': users, 'resources': Resources
    })


# Load remaining endpoints
from .user.views import *  # load user admin routes  # noqa
