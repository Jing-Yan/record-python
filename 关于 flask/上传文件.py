# -*- coding= utf-8 -*-

import os
from flask import Flask, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

# 文件路径
UPLOAD_FOLDER = 'D:/codes/PycharmProjects/untitled1/path'
# 文件格式
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'jpg', 'jpeg', 'gif', 'png', 'JPG', 'docx', 'xls', 'csv', 'doc'])

app = Flask(__name__)
# 注册文件路径
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# 限制文件大小
app.config['MAX_CONTENT_LENGTH'] = 10*1024*1024


def allowed_file(filename):
    return '.' in filename and filename.split('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            # 在将文件保存在文件系统之前，要坚持使用这个 secure_filename() 函数来确保文件名是安全的
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''


@app.route('/uploads/<filename>', methods=['GET', 'POST'])
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run()

