# -*- coding: UTF-8 -*-

from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
from celery.schedules import timedelta
import urllib

class Config:

    # mongo 链接信息
    MONGODB_HOST = '192.168.0.188'
    MONGODB_PORT = 27017
    MONGODB_USERNAME = 'root'
    MONGODB_PASSWORD = 'root1234'
    MONGODB_URL = 'mongodb://{0}:{1}'.format(MONGODB_HOST, MONGODB_PORT)
    # MONGODB_URL='mongodb://{0}:{1}@{2}:{3}'.format(MONGODB_USERNAME,MONGODB_PASSWORD,MONGODB_HOST,MONGODB_PORT)
