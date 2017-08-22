# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')

from .default import Config

class TestConfig(Config):
    pass