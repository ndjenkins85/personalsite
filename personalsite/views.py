# Copyright © 2025 by Nick Jenkins. All rights reserved

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
from pathlib import Path
import random
from typing import Any, Dict, List

# coding: utf-8
from flask import current_app, make_response, render_template, request
from pytz import timezone as tzoffset
import markdown
from markupsafe import Markup

from personalsite import app
from personalsite import article_parsing, resume_parsing


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
    base_template_path = Path("personalsite/resume/base_template.md")
    base_template = base_template_path.read_text()

    base_template = resume_parsing.clear_expansions_for_one_pager(base_template)
    resume_data = Markup(markdown.markdown(base_template))  # NOQA: S704

    return render_template("resume_v2.html", resume_data=resume_data)


# @app.route("/resume/dynamic")
# def resume_dynamic_form() -> str:
#     """Flask route to display dynamic resume form.

#     Returns:
#         str: rendered resume page
#     """
#     return render_template("resume_dynamic_form.html")


@app.route("/resume/dynamic/<path:path>")
def resume_dynamic(path: str) -> str:
    """Flask route to display resume.

    Args:
        path: str job name

    Returns:
        str: rendered resume page
    """
    base_template_path = Path("personalsite/resume/base_template.md")
    base_template = base_template_path.read_text()

    expansions = {
        r"{expansive_summary}": resume_parsing.get_expansive_summary(path),
        r"{expansive_tiktok}": resume_parsing.get_expansive_tiktok(path),
        r"{expansive_bcg}": resume_parsing.get_expansive_bcg(path),
        r"{expansive_page_break}": resume_parsing.get_expansive_page_break(),
        r"{expansive_additional}": resume_parsing.get_expansive_additional(),
    }

    for key, value in expansions.items():
        base_template = base_template.replace(key, value)

    resume_data = Markup(markdown.markdown(base_template))  # NOQA: S704

    return render_template("resume_v2.html", resume_data=resume_data)


@app.route("/cover/dynamic/<path:path>")
def cover_dynamic(path: str) -> str:
    """Flask route to display dynamic resume.

    Args:
        path: str job name

    Returns:
        str: rendered resume page
    """
    cover_letter_path = Path("data/jobs", path, "cover_letter.md")
    cover_letter = cover_letter_path.read_text()

    cover_letter = Markup(markdown.markdown(cover_letter))  # NOQA: S704

    return render_template("resume_v2.html", resume_data=cover_letter)


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
    filters["tags"] = request.args.get("tags", "")
    if request.args.get("year", ""):
        filters["year"] = request.args.get("year", "")

    # Article URL always follows this structure
    # Add filters for each part that exists in path
    routes = ["major_type", "year", "month", "day", "title"]
    breadcrumbs = path.split("/")
    for ind, val in enumerate(breadcrumbs):
        filters[routes[ind]] = val

    articles = article_parsing.parse_all_articles_against_filters(filters)
    # Determines whether to display a single article or multiple summaries
    single = len(breadcrumbs) == 5 and len(articles) == 1

    if single:
        related_articles = article_parsing.get_related_articles(articles[0])
    else:
        related_articles = []

    tags = article_parsing.get_all_tags()

    return render_template(
        "articles.html",
        articles=articles,
        routes=routes,
        breadcrumbs=breadcrumbs,
        single=single,
        tags=tags,
        related_articles=related_articles,
    )


@app.route("/sitemap.xml", methods=["GET"])
def sitemap() -> Any:  # NOQA: ANN401
    """Generate sitemap.xml. Makes a list of urls and date modified.

    Returns:
        Any: rendered sitemap.xml
    """
    pages = []
    ten_days_ago = (dt.now() - timedelta(days=10)).date().isoformat()
    # static pages
    for rule in current_app.url_map.iter_rules():
        if rule.methods and "GET" in rule.methods:
            if len(rule.arguments) == 0:
                pages.append([rule.rule, ten_days_ago])

    articles = article_parsing.parse_all_articles()
    for article in articles:
        pages.append(["/articles/" + article["url_helper"], article["date"]])  # type: ignore

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

    def inti(d: Any) -> int:  # NOQA: ANN401
        return int(d)

    def utc_to_local(time: Any, offset_str: Any) -> Any:  # NOQA: ANN401
        """Converts universal time to local.

        Args:
            time (Any): time variable
            offset_str (Any): offset string

        Returns:
            Any: adjusted time
        """
        adjusted = time.replace(tzinfo=timezone.utc).astimezone(tz=tzoffset(offset_str))
        return adjusted.strftime("%Y-%m-%d at %H:%M:%S")

    def tag_years() -> List[int]:
        """Get list of years from 2017.

        Returns:
            List[int]: List of years
        """
        years = list(range(2017, dt.now().year + 1))  # type: ignore
        return years

    def years_months(date: str) -> str:
        """Calculates years and months since date.

        Args:
            date (str): yyyy-mm-dd

        Returns:
            str: formatted string
        """
        days = (dt.now() - dt.strptime(date, "%Y-%m-%d")).days
        return f"{days // 365}y {(days % 365) // 30}m"

    def get_carousel_items() -> List[str]:
        """Resolves the static carousel directory for valid JPEG links.

        Returns:
            List[str]: string path to files
        """
        items = ["carousel/" + str(x.name) for x in Path("personalsite", "static", "carousel").glob("*.jpeg")]
        random.shuffle(items)
        return items

    return dict(
        deci=deci,
        inti=inti,
        utc_to_local=utc_to_local,
        tag_years=tag_years,
        years_months=years_months,
        get_carousel_items=get_carousel_items,
    )
