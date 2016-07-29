#!/usr/bin/env python

import os
import datetime
import flask
from flask import Flask, request, redirect, render_template
import csv
from io import TextIOWrapper

# This module is a Flask app, which can handle HTTP requests for a WSGI server
app = Flask(__name__.split('.')[0])
app.debug = os.environ.get('DEBUG')
app.template_folder = os.path.realpath(os.path.join(__file__,'..','..','templates'))
app.static_folder = os.path.realpath(os.path.join(__file__,'..','..','static'))

@app.route('/')
def index():
    return render_template('index.html')
