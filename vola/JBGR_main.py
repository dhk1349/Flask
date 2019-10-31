# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 13:36:14 2019

@author: dhk13
"""

import sys
from flask import Flask,render_template, g, request, redirect
#import volatility.conf as conf

#config = conf.ConfObject()
app=Flask(__name__)

@app.route('/', methods=['GET','POST'])
def initial_info():
    if request.method == 'POST':
        g.location=request.form['location']
        g.image="Win7SP0x64"
    return render_template('index.html')
    #return redirect(url_for(pass_info))

@app.route('/main')
def pass_info():
    #vol.py -f training.vmem --profile=Win7... pslist
    """
    if sys.version_info < (2, 6, 0):
        sys.stderr.write("Volatility requires python version 2.6, please upgrade your python installation.")
        sys.exit(1)
    config.add_option("INFO", default = None, action = "store_true",
                  cache_invalidator = False,
                  help = "Print information about all registered objects")
    config.set_usage(usage = "Volatility - A memory forensics analysis platform.")
    config.add_help_hook(list_plugins)
    """

if __name__=="__main__":
    app.run()