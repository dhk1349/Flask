# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 13:36:14 2019

@author: dhk13
"""


from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

if __name__=="__main__":
    app.run()