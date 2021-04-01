from flask import Flask
from flask_cors import *

# 创建webapp应用,__name__是python预定义变量，被设置为使用本模块.
webapp = Flask(__name__)
CORS(webapp, supports_credentials=True)

# 此处对应了路由文件routes.py中的内容
from app import routes

