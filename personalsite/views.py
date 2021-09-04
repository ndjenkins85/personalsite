# Copyright © 2021 by Nick Jenkins. All rights reserved
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from datetime import datetime as dt
from datetime import timedelta, timezone

# coding: utf-8
from flask import current_app, make_response, render_template, request
from pytz import timezone as tzoffset

from personalsite import app
from personalsite.file_parsing import get_all_files, get_all_tags, parse_files_and_filters


@app.context_processor
def get_master_details():
    """General calculation tools for use in Jinja pages."""

    def deci(myfloat):
        return "{:.1%}".format(myfloat)

    def inti(d):
        return int(d)

    def utc_to_local(time=None, offset_str=None):
        try:
            adjusted = time.replace(tzinfo=timezone.utc).astimezone(tz=tzoffset(offset_str))
            return adjusted.strftime("%Y-%m-%d at %H:%M:%S")
        except:
            return None

    return dict(deci=deci, inti=inti, utc_to_local=utc_to_local)


@app.route("/")
def home():
    """Flask route to display home page."""
    return render_template("index.html", tags=get_all_tags())


@app.route("/resume")
def resume():
    """Flask route to display resume."""
    return render_template("resume.html")


@app.route("/sitemap.xml", methods=["GET"])
def sitemap():
    """Generate sitemap.xml. Makes a list of urls and date modified."""
    pages = []
    ten_days_ago = (dt.now() - timedelta(days=10)).date().isoformat()
    # static pages
    for rule in current_app.url_map.iter_rules():
        if (
            "GET" in rule.methods
            and len(rule.arguments) == 0
            and rule.rule.replace("/", "") not in app.config["SITEMAP_EXCLUDES"]
        ):
            pages.append([rule.rule, ten_days_ago])

    files = get_all_files()
    for f in files:
        pages.append(["/articles/" + f["url_helper"], f["date"]])

    sitemap_xml = render_template("sitemap_template.xml", pages=pages, siteurl=app.config["SITEURL"])
    response = make_response(sitemap_xml)
    response.headers["Content-Type"] = "application/xml"
    return response


@app.route("/articles/", defaults={"path": ""})
@app.route("/articles/<path:path>")
def articles(path):
    """Flask route for articles parsing and display.

    Loads all available articles into memory.
    Parses the full url `path` into a list of filters.

    Displays article summaries when more than one article filtered.
    Displays article full text when only one article selected.
    """
    routes = ["major_type", "year", "month", "day", "title"]

    filters = {}
    filters["tags"] = request.args.get("tags", None)
    if request.args.get("year", None):
        filters["year"] = request.args.get("year")

    if request.args.get("major_type", None):
        filters["major_type"] = request.args.get("major_type")

    try:
        int(request.args.get("page", "0"))
    except:
        pass

    breadcrumbs = path.split("/")
    for ind, val in enumerate(breadcrumbs):
        filters[routes[ind]] = val

    files = parse_files_and_filters(filters)

    single = len(breadcrumbs) == 5 and len(files) == 1

    return render_template(
        "articles.html", files=files, routes=routes, breadcrumbs=breadcrumbs, single=single, tags=get_all_tags()
    )
