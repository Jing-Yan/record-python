# -*- coding:utf-8 -*-

from flask import Flask, session, render_template, jsonify, request
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Email, Length
from flask_bootstrap import Bootstrap
import random, os, StringIO

app = Flask(__name__)


def generator_validate_code():
    width = 60 * 4
    height = 60
    color = (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
    text = ''
    image = Image.new('RGB', (width, height), (255, 255, 255))
    font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 36)
    draw = ImageDraw.Draw(image)
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=color)

    for i in range(4):
        char = chr(random.randint(65, 90))
        text += char
        font_color = (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
        draw.text((60 * i + 10, 10), char, font=font, fill=font_color)
    image = image.filter(ImageFilter.EMBOSS)
    # path = os.path.join('static/image/code', text)
    # image.save(path, 'JPEG')
    return image, text


class RegisterForm(FlaskForm):
    """ 注册表单"""

    username = StringField(u'姓名', validators=[DataRequired(), Length(1, 32)])
    email = StringField(u'邮箱', validators=[DataRequired(), Email()])
    password = PasswordField(u'密码', validators=[DataRequired(), Length(6, 32, message='密码长度6-32位')])
    password1 = PasswordField(u'确认密码', validators=[DataRequired(), Length(6, 32, message='密码长度6-32位'), EqualTo('password', message='密码必须一致')])
    verification_code = StringField(u'', validators=[DataRequired(), Length(4, message='请输入4位数的验证码')])
    submit = SubmitField(u'注册')

bootstrap = Bootstrap()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess'
bootstrap.init_app(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/register')
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        pass
    return render_template("register.html", form=form)


@app.route('/code/')
def code():
    # 这个是保存到内存当中，不用保存在磁盘
    code_img, code_text = generator_validate_code()
    buf = StringIO.StringIO()
    code_img.save(buf, 'JPEG', quality=70)
    session['code_text'] = code_text
    buf_str = buf.getvalue()
    response = app.make_response(buf_str)
    response.headers['Content-Type'] = 'image/jpeg'
    print code_img, code_text
    return response


tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


if __name__ == '__main__':
    app.run()
