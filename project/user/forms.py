# !/usr/bin/python
# -*- coding: utf-8 -*-
""" Created by andresilva on 2/21/16"""
from flask_wtf import FlaskForm
import mongoengine as me
import wtforms as wtf
import wtforms.validators as v

import project.user.models as umodels


class LoginForm(FlaskForm):
    username = wtf.StringField('Username', validators=[v.DataRequired()])
    password = wtf.PasswordField('Password', validators=[v.DataRequired()])


class RegisterForm(FlaskForm):
    username = wtf.StringField('Username', validators=[v.DataRequired()])
    password = wtf.PasswordField('Password', validators=[v.DataRequired()])
    confirm_password = wtf.PasswordField('Confirm Password', validators=[
        v.DataRequired(), v.EqualTo('password')])

    def validate_username(form, field):
        username = field.data
        try:
            umodels.User.objects.get(username=username)
            raise v.ValidationError("Username \"{}\" already exists. "
                                    "".format(username))
        except me.DoesNotExist:
            pass
        return username
