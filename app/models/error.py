# -*- coding: UTF-8 -*-
class DataException (Exception):
    def __init__(self, err='缺少相关参数或参数不正确'):
        Exception.__init__(self, err)


class DocumentException (Exception):
    def __init__(self, err='文档不存在'):
        Exception.__init__(self, err)


class UserUnAuthorized(Exception):
    def __init__(self, err='用户权限不足'):
        Exception.__init__(self, err)


class UserEmailRegex(Exception):
    def __init__(self, err='邮箱不存在'):
        Exception.__init__(self, err)


class UserNotExists(Exception):
    def __init__(self, err='用户不存在'):
        Exception.__init__(self, err)
