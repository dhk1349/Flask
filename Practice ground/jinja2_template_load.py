# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 14:05:19 2019

@author: dhk13
"""

from jinja2 import Environment, FileSystemLoader

file_loader=FileSystemLoader('templates')
env=Environment(loader=file_loader)

template=env.get_template('hello_world.txt')
template.render()

#위 같은 식으로 사용이 가능

template=env.get_template("if.txt")
template.render(truth=True)

person={}
person['name']="dhk1349"
person['salary']=999
template=env.get_template("personal_info.txt")
template.render(data=person)