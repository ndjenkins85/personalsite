# coding: utf-8
from flask import Flask, g, flash, render_template, redirect, url_for, request, jsonify, session, make_response, abort, current_app
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug import secure_filename

import os
import io
import json
import requests
import pandas as pd

from pytz import timezone as tzoffset
from datetime import timezone, timedelta
from datetime import datetime as dt

from personalsite import app, file_service

from personalsite.file_parsing import get_file_details, get_all_files, parse_files_and_filters


#from datamodels.load_azurefs import load_file_azure
#from analysis.file_parsing.file_read import file_read

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

##################### Basic logins and home ##########################

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/resume')
def resume():
    return render_template('resume.html')


# a route for generating sitemap.xml
@app.route('/sitemap.xml', methods=['GET'])
def sitemap():
      """Generate sitemap.xml. Makes a list of urls and date modified."""
      pages = []
      ten_days_ago = (dt.now() - timedelta(days=10)).date().isoformat()
      # static pages
      for rule in current_app.url_map.iter_rules():
          if "GET" in rule.methods and len(rule.arguments)==0 and rule.rule.replace("/","") not in app.config["SITEMAP_EXCLUDES"]:
              pages.append(
                           [rule.rule, ten_days_ago]
                           )
      sitemap_xml = render_template('sitemap_template.xml', pages=pages, siteurl=app.config["SITEURL"])
      response= make_response(sitemap_xml)
      response.headers["Content-Type"] = "application/xml"        
      return response


@app.route('/articles/', defaults={'path': ''})
@app.route('/articles/<path:path>')
def articles(path):

    filters = {"tags": request.args.get("tags", None)}

    try:
        page = int(request.args.get("page", "0"))
    except:
        page = 0

    routes = ["major_type", "year", "month", "day", "title"]
    breadcrumbs = path.split("/")
    for ind, val in enumerate(breadcrumbs):
        filters[routes[ind]] = val

    files = parse_files_and_filters(filters)

    return render_template('articles.html', files=files, routes=routes, breadcrumbs=breadcrumbs)


#    articles/professional/2018/01/25/data-service-productisation_building



# @app.route('/articles')
# def filter_articles():
#     filters = {"major_type": request.args.get("major_type", None), 
#                "period": request.args.get("period", None), 

#     try:
#         page = int(page)
#     except:
#         page = 0


#     files = parse_files_and_filters(filters)

#     if len(files)==1:
#         f = files[0]
#         return redirect(url_for('get_article', major_type=f["major_type"], year=f["year"], 
#                 month=f["month"], day=f["day"], title=f["title"]))
#     elif len(files)==0:
#         flash("No articles match those filters") 
#         return redirect(url_for('home'))


#     files = [f["filename"] for f in files]



#     return render_template('articles.html', files=files)


# @app.route('/articles/<major_type>/<year>/<month>/<day>/<title>')
# def get_article(major_type, year, month, day, title):
    
#     filters = {"major_type": request.view_args.get('major_type', None), 
#                "year": request.view_args.get('year', None), 
#                "month": request.view_args.get('month', None), 
#                "day": request.view_args.get('day', None), 
#                "title": request.view_args.get('title', None)}

#     files = parse_files_and_filters(filters)
#     files = [f["filename"] for f in files]
#     return '<br>'.join(files)





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

