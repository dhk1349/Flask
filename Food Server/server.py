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
conn=sqlite3.connect("./database/food.db", check_same_thread=False )
cur=conn.cursor()

@app.route('/')
def index():

    return render_template("main.html")


@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        menu=request.form['name']
        option=request.form['method']
        
        if option=="food":
            query="select * from food where food=?"
            
        elif option=="ingred":
            query="select * from food where ingred=?"
        print(menu)
        cur.execute(query, (menu,))
        rows=cur.fetchall()
    return render_template("result.html", result=rows, option=option)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        data=request.form
        """
        중복 여부 확인 추가 할 것
        """
        query="insert into food(food, ingred) values(?,?)"

        cur.execute(query, ())
        conn.commit()

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
    conn.close()