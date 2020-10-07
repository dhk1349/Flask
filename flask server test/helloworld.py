# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 23:32:03 2020

@author: dhk13
"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()