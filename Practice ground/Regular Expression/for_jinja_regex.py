# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 12:49:37 2019

@author: dhk13
"""

from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def temp_test():
    return render_template('jinja_regex.html', my_string="This is test file for jinja regex", my_list=["pear", "apple", "pen"])

if __name__=="__main__":
    app.run()