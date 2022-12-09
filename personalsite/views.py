# Copyright © 2023 by Nick Jenkins. All rights reserved

"""Contains main flask website routes and helper functions.

Routes correspond to templates/*.html

* Home page (index.html)
* Resume
* Articles

Helper functions for sitemap and jinja python enablement.
"""

# Copyright © 2023 by Nick Jenkins. All rights reserved

from datetime import datetime as dt
from datetime import timedelta, timezone
from typing import Any, Dict, List

# coding: utf-8
from flask import current_app, make_response, render_template, request
from pytz import timezone as tzoffset

from personalsite import app
from personalsite import article_parsing


@app.route("/")
def home() -> str:
    """Flask route to display home page.

    Returns:
        str: rendered home page as text
    """
    return render_template("index.html", tags=article_parsing.get_all_tags())


@app.route("/resume")
def resume() -> str:
    """Flask route to display resume.

    Returns:
        str: rendered resume page
    """
    return render_template("resume.html")


@app.route("/articles/", defaults={"path": ""})
@app.route("/articles/<path:path>")
def articles(path: str) -> str:
    """Flask route for articles parsing and display.

    Loads all available articles into memory.
    Parses the full url `path` into a list of filters.

    Displays article summaries when more than one article filtered.
    Displays article full text when only one article selected.

    Args:
        path (str): additional string URL path

    Returns:
        str: rendered article pages
    """
    # Fill filters dict with what is in the URL; params
    filters: Dict[str, str] = {}
    filters["tags"] = request.args.get("tags", None)
    if request.args.get("year", None):
        filters["year"] = request.args.get("year")

    # Article URL always follows this structure
    # Add filters for each part that exists in path
    routes = ["major_type", "year", "month", "day", "title"]
    breadcrumbs = path.split("/")
    for ind, val in enumerate(breadcrumbs):
        filters[routes[ind]] = val

    articles = article_parsing.parse_all_articles_against_filters(filters)
    # Determines whether to display a single article or multiple summaries
    single = len(breadcrumbs) == 5 and len(articles) == 1

    tags = article_parsing.get_all_tags()

    return render_template(
        "articles.html", articles=articles, routes=routes, breadcrumbs=breadcrumbs, single=single, tags=tags
    )


@app.route("/sitemap.xml", methods=["GET"])
def sitemap() -> Any:
    """Generate sitemap.xml. Makes a list of urls and date modified.

    Returns:
        Any: rendered sitemap.xml
    """
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

    articles = article_parsing.parse_all_articles()
    for article in articles:
        pages.append(["/articles/" + article["url_helper"], article["date"]])

    sitemap_xml = render_template("sitemap_template.xml", pages=pages, siteurl=app.config["SITEURL"])
    response = make_response(sitemap_xml)
    response.headers["Content-Type"] = "application/xml"
    return response


@app.context_processor
def get_master_details() -> Dict[Any, Any]:
    """General calculation tools for use in Jinja pages.

    Returns:
        Dict[Any, Any]: collection of functions
    """

    def deci(myfloat: float) -> str:
        return "{:.1%}".format(myfloat)

    def inti(d: Any) -> int:
        return int(d)

    def utc_to_local(time: Any, offset_str: Any) -> Any:
        """Converts universal time to local.

        Args:
            time (Any): time variable
            offset_str (Any): offset string

        Returns:
            Any: adjusted time
        """
        adjusted = time.replace(tzinfo=timezone.utc).astimezone(tz=tzoffset(offset_str))
        return adjusted.strftime("%Y-%m-%d at %H:%M:%S")

    def tag_years() -> List[str]:
        """Get list of years from 2017."""
        return list(range(2017, dt.now().year + 1))

    def years_months(date: str) -> str:
        """Calculates years and months since date."""
        days = (dt.now() - dt.strptime(date, "%Y-%m-%d")).days
        return f"{days // 365}y {(days % 365) // 30}m"

    return dict(deci=deci, inti=inti, utc_to_local=utc_to_local, tag_years=tag_years, years_months=years_months)
