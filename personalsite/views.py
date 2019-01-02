# coding: utf-8
from flask import Flask, g, flash, render_template, redirect, url_for, request, jsonify, session, make_response, abort
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug import secure_filename

import os
import io
import json
import requests
import pandas as pd

from pytz import timezone as tzoffset
from datetime import timezone
from datetime import datetime as dt

from personalsite import app, file_service

#from datamodels.load_azurefs import load_file_azure
#from analysis.file_parsing.file_read import file_read

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

##################### Basic logins and home ##########################


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login')
def login():    
    #user = Users.query.filter_by(email=email).first()
    user = None
    login_user(user)
    return redirect(url_for('home'))    


@app.route('/logout')
def logout():
    logout_user()
    flash('Logged out')
    return redirect(url_for('home'))  


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)


def allowed_file(filename):
    return '.' in filename and filename.lower().rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.context_processor
def get_master_details():
    def deci(myfloat):
        return '{:.1%}'.format(myfloat)
    def inti(d):
        return int(d)

    def utc_to_local(time=None, offset_str=None):
        try:
            adjusted = time.replace(tzinfo=timezone.utc).astimezone(tz=tzoffset(offset_str)) 
            return adjusted.strftime("%Y-%m-%d at %H:%M:%S")
        except:
            return None

    return dict(deci=deci, inti=inti, utc_to_local=utc_to_local)

###################### File uploads ##########################
@app.route('/dropzoneredirect', methods=['POST'])
def upload():
    uploaded_file = request.files.get('myfileinput')
    random_id = "xxxx" # TODO

    if uploaded_file and allowed_file(uploaded_file.filename):

        # create filename, prefixed with datetime
        filename_uuid = str(random_id)
        filename_part = secure_filename(uploaded_file.filename)
        file_name = filename_uuid + "-" + filename_part

        file_service.create_file_from_bytes(
            share_name='user-uploads', directory_name=None, 
            file_name=file_name, file=uploaded_file.stream.read())

        return redirect(url_for('home'))


@app.route('/version')
def version():
    return app.config["VERSION"]


@app.route('/dropzoneredirect')
@login_required
def dropzoneredirect():
    flash("Data uploaded, please wait for file to be checked")
    return redirect(url_for('home'))

