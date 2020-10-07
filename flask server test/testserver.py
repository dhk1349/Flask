# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 22:26:04 2020

@author: dhk13
"""



import os
import sys


#from bringPoseEst import *
from flask import Flask, jsonify, request, send_file, render_template
from werkzeug.utils import secure_filename
import requests

app = Flask(__name__)



@app.route('/')
def index():
    print("pass fnc ended")
    """
    데이터를 받거나
    여기서 가공.

    """
    return render_template("index.html")

@app.route('/page1')
def p1():

    return render_template("page1.html")


@app.route('/page2')
def p2():

    return render_template("page2.html")


@app.route('/page3')
def p3():

    
    return render_template("page3.html")


@app.route('/page4')
def p4():

    return render_template("page4.html")

@app.route('/about')
def about():
    """
    데이터를 받거나
    여기서 가공.

    """

    return render_template("about.html")

@app.route('/users/<user>')
def enterpage(user):
    return 'hello %s' % user


@app.route('/receive', methods=['GET', 'POST'])
def reveive():
    if request.method == 'POST':
        result=request.form
        return render_template("receive.html", result=result)


@app.route('/diagnosis')
def diagnosis():
    
    return render_template("diagnosis.html")


@app.route('/my_page')
def my_page():
    return render_template("my_page.html")


@app.route('/detail')
def my_page_detail():
    return render_template("my_page_detail.html")





if __name__ == '__main__':
    app.run(debug=True)
