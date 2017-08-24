# -*- coding: UTF-8 -*-
from app.views.demo import demo
from flask import jsonify, request
from app.models.user import User
from app.models.error import DataException
@demo.route('/')
def index():
    return jsonify({'a': 1})


@demo.route('/login', methods=['POST'])
def login():
    data = request.get_josn(force=True)
    name = data.get('name', None)
    password = data.get('passwd', None)
    if name and password:
        user = User(name, password)
    else:
        raise DataException

