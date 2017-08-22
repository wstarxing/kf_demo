# -*- coding: UTF-8 -*-
from app.config.db import user
from app.models.error import UserNotExists


class User(object):
    doc = user

    def __init__(self, user_id=None):
        self.id = user_id
        self.is_exists()

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


