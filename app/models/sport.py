# -*- coding: UTF-8 -*-
from app.config.db import sport_list


class Sport(object):

    doc = sport_list

    def __init__(self):
        pass

    def get_sport(self):
        pass

    def add_sport(self):
        pass

    def del_sport(self):
        pass

    def modify_sport(self):
        pass


class SportPublic(Sport):
    pass


class SportPerson(Sport):
    pass