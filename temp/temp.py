# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 17:09:36 2019

@author: dhk13
"""

from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def temp_test():
    return render_template("temp_inheritance_html.html",my_list=[10,9,8,7,6,5,4,3,2,1])

if __name__=="__main__":
    app.run()