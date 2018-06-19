# !/usr/bin/python
# -*- coding: utf-8 -*-
"""Created by andresilva on 7/25/16"""
from flask_wtf import FlaskForm
import wtforms as wtf
import wtforms.validators as v
import mongoengine as me
import project.user.models as umodels


class CreateForm(FlaskForm):
    username = wtf.StringField('Username', validators=[v.DataRequired()])
    password = wtf.PasswordField('Password', validators=[v.DataRequired()])
    is_admin = wtf.BooleanField("Is Admin")

    def validate_username(form, field):
        username = field.data
        try:
            umodels.User.objects.get(username=username)
            raise v.ValidationError("Username \"{}\" already exists. "
                                    "".format(username))
        except me.DoesNotExist:
            pass
        return username
