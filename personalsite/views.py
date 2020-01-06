# coding: utf-8
from flask import Flask, render_template, request, make_response, current_app

from pytz import timezone as tzoffset
from datetime import timezone, timedelta
from datetime import datetime as dt

from personalsite import app
from personalsite.file_parsing import get_file_details, get_all_files, parse_files_and_filters, get_all_tags


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


@app.route('/')
def home():
    return render_template('index.html', tags=get_all_tags())


@app.route('/resume')
def resume():
    return render_template('resume.html')
    

@app.route('/sitemap.xml', methods=['GET'])
def sitemap():
    """Generate sitemap.xml. Makes a list of urls and date modified."""
    pages = []
    ten_days_ago = (dt.now() - timedelta(days=10)).date().isoformat()
    # static pages
    for rule in current_app.url_map.iter_rules():
        if "GET" in rule.methods and len(rule.arguments)==0 and rule.rule.replace("/","") not in app.config["SITEMAP_EXCLUDES"]:
            pages.append([rule.rule, ten_days_ago])

    files = get_all_files()
    for f in files:
        pages.append(["/articles/" + f["url_helper"], f["date"]])
    
    sitemap_xml = render_template('sitemap_template.xml', pages=pages, siteurl=app.config["SITEURL"])
    response= make_response(sitemap_xml)
    response.headers["Content-Type"] = "application/xml"        
    return response


@app.route('/articles/', defaults={'path': ''})
@app.route('/articles/<path:path>')
def articles(path):

    filters = {}
    filters["tags"] = request.args.get("tags", None)
    if request.args.get("year", None):
        filters["year"] = request.args.get("year")
    
    if request.args.get("major_type", None):
        filters["major_type"] = request.args.get("major_type")

    try:
        page = int(request.args.get("page", "0"))
    except:
        page = 0

    routes = ["major_type", "year", "month", "day", "title"]
    breadcrumbs = path.split("/")
    for ind, val in enumerate(breadcrumbs):
        filters[routes[ind]] = val

    files = parse_files_and_filters(filters)

    single = (len(breadcrumbs)==5 and len(files)==1)

    return render_template('articles.html', files=files, routes=routes, breadcrumbs=breadcrumbs, 
                            single=single, tags=get_all_tags())


