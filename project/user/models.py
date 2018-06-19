# !/usr/bin/python
# -*- coding: utf-8 -*-
""" Created by andresilva on 2/19/16"""
import random
import string
import mongoengine as me
from werkzeug.local import LocalProxy

from flask_login import UserMixin, AnonymousUserMixin
from flask_bcrypt import generate_password_hash


class User(UserMixin, me.Document):
    """"""
    username = me.StringField(required=True, unique=True)
    password = me.BinaryField(required=True)
    api_key = me.StringField(required=False)
    is_admin = me.BooleanField(default=False)

    _is_deleted = me.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.username)

    def __repr__(self):
        return "<User: {}>".format(str(self))

    meta = {
        # 'allow_inheritance': True,
        'indexes': [
            ('username',),
        ],
    }

    @me.queryset_manager
    def _objects(doc_cls, queryset):
        """Original queryset manager for this object that return every
        collection available in the database"""
        return queryset

    @me.queryset_manager
    def objects(doc_cls, queryset):
        """Hides all "deleted" users from every query"""
        return queryset.filter(_is_deleted=False)

    def save(self, *args, **kwargs):
        """"""
        return super(User, self).save(*args, **kwargs)

    def delete(self, force=False):
        """Only delete user from database if the flag "force" is True"""
        if not force:
            self._is_deleted = True
            self.save()
            return None
        return super(User, self).delete()

    def _generate_api_key(self, size=64):
        """for given size, generate random string with all ascii and digits"""
        return ''.join(random.choice(string.ascii_lowercase + string.digits)
                        for _ in range(size))

    def reset_password(self, new_password="password"):
        """"""
        self.password = generate_password_hash(new_password)
        self.save()

    @classmethod
    def get_user(cls, user):
        """Get user object:
        1º check if user is already User, LocalProxy, or AnnonymousUser object
            if so, just return it
        2º if not, search for this user and return if found.
        3º otherwise, return DoesNotExists exception"""
        if any([isinstance(user, obj) for obj in [UserMixin,
                                                  AnonymousUserMixin]]):
            return user
        if isinstance(user, LocalProxy):
            return user._get_current_object()
        try:
            return User.objects.get(username=user)
        except (me.DoesNotExist, me.ValidationError):
            return User.objects.get(id=user)

    @classmethod
    def create(cls, username, password, generate_api_key=True,
               *args, **kwargs):
        """Aux method to create user MongoObject"""
        kwargs.update(dict(
            username=username,
            password=password
        ))
        user = User(**kwargs)
        user.reset_password(new_password=password)
        user.save()

        if generate_api_key:
            user.api_key = user._generate_api_key()
            user.save()
        return user
