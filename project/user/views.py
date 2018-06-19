# !/usr/bin/python
# -*- coding: utf-8 -*-
""" Created by andresilva on 2/19/16"""

from flask import redirect, render_template, request, url_for, Blueprint
from flask_login import (login_user, login_required, logout_user,
                         current_user)
from flask_bcrypt import check_password_hash

import project.user.forms as uforms
import project.user.models as umodels
import project.utils.flash as flash

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/settings/', methods=['GET'])
@login_required
def settings():
    flash.info('Welcome to your dashboard {}.'.format(str(current_user)))
    return render_template('user/settings.html')


@user_blueprint.route('/sign-in/', methods=['GET', 'POST'])
def register():
    form = uforms.RegisterForm(request.form)
    if form.validate_on_submit():
        user = umodels.User.create(form.username.data, form.password.data)
        login_user(user)
        flash.info('Welcome {}.'.format(str(user)))
        return redirect(request.args.get('next', url_for('app.home')))
    return render_template('user/register.html', form=form)


@user_blueprint.route('/login/', methods=['GET', 'POST'])
def login():
    form = uforms.LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = umodels.User.objects.filter(
                username=form.username.data).first()
            if user and check_password_hash(user.password, form.password.data):
                login_user(user)
                flash.info('Welcome {}.'.format(str(user)))
                return redirect(request.args.get('next', url_for('app.home')))
            else:
                flash.warning('Invalid Credentials. Please try again.')

    return render_template('user/login.html', form=form)


@user_blueprint.route('/logout/')
def logout():
    logout_user()
    flash.info('You were logged out.')
    return redirect(url_for('app.home'))
