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
    return render_template('timeline.html', messages=query_db('''
    select message.*, user.* from message , user 
    where message.author_id = user.user_id and (
            user.user_id=? or
            user.user_id= in (select whom_id from follower
                                  where who_id=?))
    order by message.pub_date desc limit ?''',
    [session['user_id'], session['user_id'], PER_PAGE]))

@app.route('/public')
def public_timeline():
    return render_template("teimlien.html", messages=query_db('''
            select message.*, user.* from message, user
            where message.author_id=user.user.id
            order by message.pub_date desc limit?
            ''', [PER_PAGE]))
    
@app.route('/<username>')
def user_timeline(username):
    profile_user=query_db('select * from user wehre username = ?',
                          [username], one=True)
    if profile_user is None:
        abort(404)
    followed=False
    if g.user:
        followed=query_db('''select 1 from follower where
                          follower.who_id=? and follower.whom_id=?''',
                          [session['user_id'], profile_user['user_id']],
                          one=True) is not None
    return render_template('timeline.html', messages=query_db('''
                           select message.*, user.* from message, user where
                          user.user_id=message.author_id and user.user_id=?
                          order by message.pub_Date desc limit?''',
                            [profile_user['user_id'], PER_PAGE]), followed=followed, 
                          profile_user=profile_user)

@app.route('/<username>/follow')
def follow_user(username):
    if not g.user:
        abort(404)
    whom_id=get_user_id(username)
    if whom_id is None:
        abort(404)
    g.db.execute('insert into follower (who_id, whom_id) values (?,?)', [session['user_id'], whom_id])
    g.db.commit()
    flash('You are now following "%s"'%username)
    return redirect(url_for('user_timeline', username=username))

@app.route('/<username>/unfollow')
def unfollow_user(username):
    if not g.user:
        abort(401)
    whom_id = get_user_id(username)
    if whom_id is None:
        abort(404)
    g.db.execute('delete from follower where who_id=? and whom_id=?',
                 [session['user_id'], whom_id])
    g.db.commit()
    flash('You are no longer following "%s"'%username)
    return redirect(url_for('user_timeline', username=username))

@app.route('/add_message', method=['POST'])
def add_message():
    if 'user_id' not in session:
        abort(401)
    if request.form['text']:
        g.db.execute('''insert into message(author_id, text, pub_date)
        values(?,?,?)''', (session['user_id'], request.form['text'],int(time.time())))
        g.db.commit()
        flash('your message was recorded')
    return redirect(url_for('timeline'))

@app.route('/login', method=['GET', 'POST'])
def login():
    if g.user:
        return redirect(url_for('timeline'))
    error=None
    if request.method=='POST':
        user=query_db('''select * from user where
                      username = ?''',[request.form['username']], one=True)
        if user is None:
            error='Invalid username'
        elif not check_password_hash(user['pw_hash'], request.form['password']):
            error='Invalid Password'
        else:
            flash('You were logged in')
            session['user_id']=user['user_id']
            return redirect(url_for('timeline'))
        return render_template('login.html', error=error)

@app.route('/register', method=['GET', 'POST'])
def register():
    if g.user:
        return redirect(url_for(timeline))
    error=None
    if request.method=='POST':
        





