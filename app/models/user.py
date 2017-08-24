# -*- coding: UTF-8 -*-
from flask import session
from flask_login import login_user, logout_user, UserMixin
from app.config.db import user
from app.models.error import UserNotExists


class User(object, UserMixin):
    doc = user

    def __init__(self, name=None, passwd=None, user_id=None):
        self.id = user_id
        self.name = name
        self.passwd = passwd
        # self.is_exists()

    def get_user(self):
        pass

    def add_user(self):
        pass

    def del_user(self):
        pass

    def modify_user(self):
        pass

    def is_exists(self):
        try:
            user_info = self.doc.find_one({'_id': self.id})
            for name, value in user_info.items():
                setattr(self, name, value)
        except Exception as e:
            print e
            raise UserNotExists

    def is_veritied(self):
        user = self.doc.user.find_one({'name': self.name})
        if user.get('password', None) == self.passwd:
            self.id = str(user['_id'])
            self.login()
            return True
        else:
            return False

    @staticmethod
    def is_authenticated():
        return True

    @staticmethod
    def is_active():
        return True

    @staticmethod
    def is_anonymous():
        return True

    def get_id(self):
        return unicode(self.id)

    def login(self):
        login_user(self)

    @staticmethod
    def logout():
        for i in session.keys():
            session.pop(i)
        logout_user()
