# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 11:19:35 2019

@author: dhk13
"""

#Jinja template regex
# {%  :   block start string
# %}  :   block end string
#템플릿에서 프로그래밍의 역역을 넣기 위한 기호

# {{  :   variable start string, 변수를 출력하기 위해 시작하는 기호
# }}  :   variable end string 

# {#  :   comment start string
# #}  :   comment end string
from jinja2 import Template

template=Template("Hello {{something}}!")
template.render(something = "dhk1349")