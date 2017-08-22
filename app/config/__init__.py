# -*- coding: UTF-8 -*-

from __future__ import unicode_literals
import sys
import os
import logging
reload(sys)
sys.setdefaultencoding('utf-8')


def load_config():
    """加载配置类"""
    mode = os.environ.get('MODE')
    try:
        if mode == '':
            from .online import TestConfig
            return TestConfig
    except ImportError as e:
        logging.warning(e)
        from .default import Config
        return Config

