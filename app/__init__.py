# -*- coding: UTF-8 -*-
import os

from app.config import load_config
from flask import Flask
from flask_login import LoginManager
from flask_principal import Principal
from flask_session import Session


mode = os.environ.get('MODE')

config = load_config()
principals = Principal()
login_manager = LoginManager()
session = Session()


def create_app():
    app = Flask(__name__, template_folder='', static_url_path='', static_folder='')

    app.config.from_object(config)
    config.init_app(app)

    login_manager.init_app(app)
    principals.init_app(app)
    session.init_app(app)

    from app.views.demo import demo
    app.register_blueprint(demo, url_prefix='/api')

    print u'当前环境变量', mode
    print u'使用数据库地址', config.DATABASE_URL

    return app
