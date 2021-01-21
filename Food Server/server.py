# -*- coding: utf-8 -*-
"""
Created on  2021

@author: dhk13
"""

import os
import sys
import sqlite3
from flask import Flask, jsonify, request, send_file, render_template
from werkzeug.utils import secure_filename
import requests

app = Flask(__name__)

#connecting database
conn=sqlite3.connect("./database/food.db")
cur=conn.cursor()

@app.route('/')
def index():

    return render_template("main.html")


@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        data=request.form
        option=request.form['method']
        
        if option=="food":
            query="select * from food where ingred=?"
            
        elif option=="ingred":
            query="select * from ingred where food=?"
        
        cur.execute(query, (data['name']))
        rows=cur.fetchall()
    return render_template("result.html", result=rows)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        data=request.form
        option=request.form['method']
        
        if option=="food":
            query="insert into food(food, ingred) value(?,?)"
            
        elif option=="ingred":
            query="insert into ingred(ingred, food) value(?,?)"
        
        cur.execute(query, ())
    return render_template("add.html")

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
        box=request.form
        return render_template("receive.html", result=box)


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
    app.run(debug=True, port=8000)
