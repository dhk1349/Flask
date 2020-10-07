# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 22:33:18 2020

@author: dhk13
"""
import os
import sys

print(os.path.dirname(os.path.abspath(os.path.dirname(__file__))) + "/Server/pose_estimation")

#from bringPoseEst import *
from flask import Flask, jsonify, request, send_file, render_template
from werkzeug.utils import secure_filename
from angleCalculate import *
import tensorflow as tf
import requests


sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))) + "/Server/pose_estimation")
# from config import basedir

# import requests

app = Flask(__name__)

# app.config.from_object('config')

# 필요한 기능
# 사용자 식별 페이지
# 사진 받는 페이지
# 결과 반환하는 페이지

# 심화 기능
# Redis를 통한 login auth
'''@app.route('/l')
def hello():
    return render_template("hello.html")
    '''


@app.route('/camera')
def camera():
    return render_template("camera.html")


@app.route('/')
def index():
    print("pass fnc ended")
    """
    데이터를 받거나
    여기서 가공.

    """
    return render_template("index.html")


@app.route('/about')
def about():
    """
    데이터를 받거나
    여기서 가공.

    """

    return render_template("about.html")


@app.route('/diagnosis')
def diagnosis():
    return render_template("diagnosis.html")


@app.route('/my_page')
def my_page():
    return render_template("my_page.html")


@app.route('/detail')
def my_page_detail():
    return render_template("my_page_detail.html")


@app.route('/users/<user>')
def enterpage(user):
    return 'hello %s' % user


# 파일 업로드 처리

@app.route('/fileUpload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['사진 불러오기']
        f.save('upload/' + secure_filename(f.filename))

        pass_function("upload/myImage.jpg")
        result = []
        f = open("saveimg/1.txt", 'r')
        line = f.readline()
        loc_dict = {}
        while True:
            if line == "":
                break
            lst = line.split(" ")
            # print(lst)
            loc_dict[int(lst[0])] = [float(lst[1]), float(lst[2])]
            line = f.readline()

        result = np.array(GetAngle(txttoInput(loc_dict)))
        """
        with open('model_config.json') as json_file:
            json_config = json_file.read()
        new_model = tf.keras.models.model_from_json(json_config)
        new_model.load_weights('weights_only.h5')
        pred = new_model.predict(result)
        """
        print(result)
        tmp = {}
        tmp['0'] = str(result[0])
        tmp['1'] = str(result[1])
        tmp['2'] = str(result[2])
        print(tmp)
        r = requests.post(url="http://15.165.166.78:5000/process", data=tmp, verify=False)
        print(r.status_code)
        print(r.json())
        return render_template("diagnosis.html", result=r.json()['0'])


'''
# 파일 업로드 처리
@app.route('/camerafileUpload', methods=['GET', 'POST'])
def camera_upload_file():
    if request.method == 'POST':
        f = request.files['addphoto']
        # 저장할 경로 + 파일명
        f.save('upload/add_' + secure_filename(f.filename))

        return 'uploads 디렉토리 -> 파일 업로드 성공!'

if __name__ == '__main__':
    # 서버 실행
    app.run(debug=True)



# POST
@app.route('/api/post_some_data', methods=['POST'])
def get_text_prediction():
    """
    predicts requested text whether it is ham or spam
    :return: json
    """
    result = request.get_json()

    print("this is json input")
    print(result)
    print("\n\n\n\n\n\n")

    if len(result['text']) == 0:
        return jsonify({'error': 'invalid input'})
    return jsonify({'you sent this': result["text"]})


# Send gif files
@app.route('/send')
def send():
    return send_file('test1.gif', mimetype='image/gif')

'''

if __name__ == '__main__':
    app.run(debug=True)
