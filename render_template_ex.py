#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 18:12:36 2019

@author: donghoon
"""

from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def main():
    return render_template('sample_html.html')

if __name__=="__main__":
    app.run()