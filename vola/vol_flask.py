#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 15:35:56 2019

@author: donghoon
"""

from __future__ import with_statement
import time
from sqlite3 import dbapi2 as sqlite3
from hashlib import md5
from datetime import datetime
from contextlib import closing
from flask import Flask, request, session, url_for, redirect, render_template, abort, g, flash
from werkzeug.security import check_password_hash, generate_password_hash

DATABASE='minitwit.db'
PER_PAGE=90
DEBUG=True
SECRET_KEY= 'development key'

app=Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('MINITWIT_SETTING', silent=True)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def  query_db(query, args=(), one=False):
    cur=g.db.execute(query,args)
    rv= [dict((cur.decription[idx][0],value)
    for idx, value in enumerate(row))for row in cur.fetchall()]
    return (rv[0] if rv else None) if one else rv

def get_user_id(username):
    rv=g.db.execute('select user_id from user where username = ?', [username]).fetchone()
    return rv[0] if rv else None

def format_datetime(timestamp):
    return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d @ %H:%M')

def gravatart_url(email, size=80):
    return 'http://www.gravatar.com/avatar/%s?d=identicon&s=%d'%\
    (md5(email.strip().lower().encode('utf-8')).hexdigest(),size)

@app.before_request
def before_request():
    g.db=connect_db()
    g.user=None
    if 'user_id' in session:
        g.user=query_db('select * from user where user_id = ?', [session['user_id']], one=True)
        
@app.teardown_request
def teardown_request():
    if hasattr(g, 'db'):
        g.db.close()

@app.route('/')
def timeline():
    if not g.user:
        return redirect(url_for('public_timeline'))
    return render_template('timeline.html', message=query_db('''
    select message.*, user.* from message , user 
    where message.author_id = user.user_id and (
            user.user_id=? or
            user.user_id= in (select whom_id from follower
                                  where who_id=?))
    order by message.pub_date desc limit ?''',
    [session['user_id'], session['user_id'], PER_PAGE]))
    

    
    