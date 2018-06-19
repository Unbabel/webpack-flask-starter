# !/usr/bin/python
# -*- coding: utf-8 -*-
"""Created by andresilva on 7/8/16"""

import base64
import binascii
import mongoengine as me
from flask import current_app as app
from flask_bcrypt import check_password_hash

import project.user.models as umodels


def load_user(user_id):
    if user_id not in ['None', None]:
        try:
            user = umodels.User.objects.filter(id=user_id).first()
            return user
        except (me.DoesNotExist, me.ValidationError):
            app.logger.error("User id \"{}\" does not exist".format(user_id))
    return False


def load_user_from_request(request):
    # first, try to login using the api_key url arg
    api_key = request.args.get('api_key')
    if api_key:
        user = umodels.User.objects.filter(api_key=api_key).first()
        if user:
            return user

    # next, try to login using Basic Auth first, try apikey and then user:pass
    auth = request.headers.get('Authorization')
    if auth:
        # get bytes string instead of str representation
        auth = auth.replace('Basic ', '', 1)
        try:
            auth = bytes(auth, 'utf8')
            auth = base64.b64decode(auth)
            auth = auth.decode()
        except (TypeError, binascii.Error):
            # make byte string "Str" again
            auth = auth.decode()
        # try if auth is api_key
        user = umodels.User.objects.filter(api_key=auth).first()
        if user:
            return user
        # if not, try with username and password
        if ":" in auth:
            username, password = auth.split(":")
            user = umodels.User.objects.filter(username=username).first()
            if user and check_password_hash(user.password, password):
                return user
    # finally, return None if both methods did not login the user
    return None
