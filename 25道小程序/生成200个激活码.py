# -*- coding:utf-8 -*-

"""
随机生成 200 个激活码
然后保存到 code.txt 文件 和 数据库
"""


import random, string
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import mysql.connector

import os
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you hard guess'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:ot2SECRET@localhost:3306/book'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
SQLALCHEMY_COMMIT_ON_TEARDOWN = True

db = SQLAlchemy(app)


# 生成随机码
def generateCodes(code_amount=200, code_len=6):
    Strs = string.digits+string.letters  # 生成 a-zA-Z0-9
    print Strs
    codes = []
    while (code_amount > 0):
        code = ''.join([random.choice(Strs) for i in range(code_len)])
        if code not in codes:
            code += '\n'
            codes.append(code)
            code_amount -= 1
    return codes


# 将随机码写入codes.txt
def file_write():
    with open('code.txt', 'w') as f:
        for code in generateCodes():
            f.write(code)


class Code(db.Model):
    __tablename__ = 'codes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(128), nullable=True)


def save_mysql():
    for code in generateCodes():
        codes = Code(code=code)
        db.session.add(codes)
        try:
            db.session.commit()
        except Exception as e:
            print e
    print '传输完成'


def file_read(filename):
    # 从文件中读取每行的码
    codes = []
    with open(filename, 'r') as f:
        lines = f.readlines()
    for n in range(200):
        # 去除每行的空白符
        codes.append(lines[n].strip())
    print codes
    return codes


def store():
    codes = file_read('code.txt')
    conn = mysql.connector.connect(user='root', password='ot2SECRET', database='book', use_unicode=True)
    cursor = conn.cursor()
    cursor.execute('create table code(id INT PRIMARY KEY ,c VARCHAR (6))')
    for n in range(200):
        cursor.execute('insert into code (id,c) VALUES (%s, %s)',
                       [n+1, codes[n]])
    conn.commit()
    cursor.close()
    conn.close()
    print 'finish'

if __name__ == '__main__':
    store()


