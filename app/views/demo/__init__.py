# -*- coding: UTF-8 -*-
from __future__ import unicode_literals


from flask import Blueprint


demo = Blueprint(u'demo', __name__)

from . import views
