# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 15:13:25 2019

@author: dhk13
"""

#template inheritance
# {% extends "<부모템플릿의 이름>"%}, 
#{% block %}<대체할 코드 작성> {%endblock%}

from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def call_child():
    return render_template("child_template.html", my_string="상속 템플릿", my_list=["hi","hello"])

if __name__=="__main__":
    app.run()