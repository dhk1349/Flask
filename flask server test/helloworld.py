# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 23:32:03 2020

@author: dhk13
"""

from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/receive', methods=['GET', 'POST'])
def reveive():
    if request.method == 'POST':
        f = request.files['send']
        f.save("newfile.jpg")
        print (f)
        print(type(f))
        return "file received"
    else:
        print("not post")

if __name__ == "__main__":
    app.run(port=8000)