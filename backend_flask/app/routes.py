# 从app模块中即从__init__.py中导入创建的webapp应用
import random

from flask import render_template, jsonify
import os
from app import webapp


# BASE_PATH = 'E:/test/vueclidemo/src/static'
BASE_PATH = 'C:/MyProject/cognitive_card/frontend_vuecli/src/static'
# BASE_PATH = 'D:/cognitive_card/frontend_vuecli/src/static'


# 建立路由，通过路由可以执行其覆盖的方法，可以多个路由指向同一个方法。
@webapp.route('/')
@webapp.route('/index')
def index():
    return "Hello,World!"


# VUE图片测试
@webapp.route('/pic')
def pic():
    return render_template('pic.html')


# 目录遍历
@webapp.route('/dir', methods=['GET', 'POST'])
def list_dir():
    dir_vec = []
    base_path = BASE_PATH
    for dir_name in os.listdir(base_path):
        path = os.path.join(base_path, dir_name)
        print('name: '+dir_name)
        if os.path.isdir(path):
            dir_vec.append(dir_name)
    return jsonify(dir_vec)


# 文件遍历
@webapp.route('/folder/<root>', methods=['GET', 'POST'])
def list_file(root):
    file_vec = []
    base_path = BASE_PATH+'/'+root
    for file_name in os.listdir(base_path):
        path = os.path.join(base_path, file_name)
        print('name: '+file_name)
        if os.path.isfile(path):
            file_vec.append(file_name)
        random.shuffle(file_vec)
    return jsonify(file_vec)


# VUE图片测试
@webapp.route('/ping')
def ping():
    return jsonify('This is the string from Flask!')

