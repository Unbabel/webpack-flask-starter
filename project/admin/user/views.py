# !/usr/bin/python
# -*- coding: utf-8 -*-
""" Created by andresilva on 2/19/16"""
import mongoengine as me
from flask import redirect, abort, render_template, request, url_for
from flask_login import login_required
from project.admin.views import admin_blueprint
from project.home.decorators import admin_required

import project.admin.user.forms as auforms
import project.user.models as umodels
import project.utils.flash as flash


@admin_blueprint.route('/admin/users/create/', methods=['GET', 'POST'])
@login_required
@admin_required
def user_create(user_id=None):
    """"""
    form = auforms.CreateForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = umodels.User.create(form.username.data, form.password.data)
            # setting user admin variable
            user.is_admin = form.is_admin.data
            user.save()

            url = url_for("admin.user_detail", user_id=str(user))
            msg = ("<span>User user <a href=\"{}\">{}</a> was successfully "
                   "created.</span>".format(url, str(user)))
            flash.success(msg)
    return render_template('admin/user/create.html', form=form)


@admin_blueprint.route('/admin/user/<user_id>/', methods=['GET', 'POST'])
@login_required
@admin_required
def user_detail(user_id=None):
    """"""
    try:
        user = umodels.User.objects.get(id=user_id)
    except (me.DoesNotExist, me.ValidationError):
        abort(404)

    return render_template('admin/user/detail.html', **{'user': user})


@admin_blueprint.route('/admin/user/<user_id>/toggle/<action>',
                       methods=['GET'])
@login_required
@admin_required
def user_toggle(user_id=None, action=None):
    try:
        user = umodels.User.get_user(user_id)
        if action == "remove":
            user.delete()
            flash.success("User \"{}\" was successfully deleted!"
                          "".format(str(user)))
        elif action == "is_admin":
            user.is_admin = not user.is_admin
            user.save()
            flash.success("User \"{}\" field \"{}\" was successfully "
                          "updated to \"{}\"!".format(str(user), action,
                                                      user.is_admin))
    except (me.DoesNotExist, me.ValidationError) as e:
        flash.warning("User with id \"{}\" does not exist."
                      "".format(user_id))

    return redirect(url_for("admin.home"))
