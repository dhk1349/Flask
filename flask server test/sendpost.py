# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 15:21:19 2020

@author: dhk1349
"""

import requests
with open('send.jpg', 'rb') as f1:
    files = [
        ('send', f1)
    ]
    requests.post('http://127.0.0.1:8000/receive', files=files)
    print("sent")