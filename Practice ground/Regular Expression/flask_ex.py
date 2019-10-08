# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 20:15:26 2019

@author: dhk13
"""

from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello():
    return 'hello world!'

if __name__=="__main__":
    app.run()