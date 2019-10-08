#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 16:53:23 2019

@author: donghoon
"""

from flask import Flask

app=Flask(__name__)
@app.route('/')
def hello_world():
    return "Hello world!!"

@app.route('/user/<username>')
def get_username(username):
    return 'user: '+username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d'%post_id

if __name__=="__main__":
    app.run()