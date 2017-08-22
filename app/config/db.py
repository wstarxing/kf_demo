# -*- coding: UTF-8 -*-
from pymongo import MongoClient
from app import config

# mongodb连接器
client = MongoClient(config.MONGODB_URL, connect=False)

sport_list = client.demo.sportlist

user = client.demo.user
