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

import os
from collections import defaultdict
from operator import itemgetter

import markdown
from flask import Markup


def get_file_details(filename):
    """Parses a markdown article into python dictionary."""

    # To debug issues with 'None', remove the try except here to get info on why crashed
    assert len(filename.split(".")) == 2, f"{filename} needs 1x . character (md)"
    details, filetype = filename.split(".")

    assert len(details.split("_")) == 4, f"{filename} needs 3x '_' for date, type, title, tags"
    date, major_type, title, tags = details.split("_")

    title_cap = title.replace("-", " ").capitalize()

    if tags:
        tags = tags.split("-")
    else:
        tags = []

    year, month, day = date.split("-")

    if month in ["01", "02", "03", "04"]:
        period = f"{year}_early"
    elif month in ["05", "06", "07", "08"]:
        period = f"{year}_mid"
    elif month in ["09", "10", "11", "12"]:
        period = f"{year}_late"
    else:
        period = None

    url_helper = f"{major_type}/{year}/{month}/{day}/{title}"

    article = open_article(filename)

    teaser = article[0].replace("â€˜", "'").replace("â€™", "'")
    article = "".join(article).replace("â€˜", "'").replace("â€™", "'")

    teaser = Markup(markdown.markdown(teaser))
    article = Markup(markdown.markdown(article))
    article = article.replace("img alt", "img class=img-thumbnail alt")

    return {
        "filename": filename,
        "date": date,
        "major_type": major_type,
        "title": title,
        "tags": tags,
        "year": year,
        "month": month,
        "day": day,
        "period": period,
        "filename": filename,
        "filetype": filetype,
        "title_cap": title_cap,
        "url_helper": url_helper,
        "teaser": teaser,
        "article": article,
    }


def open_article(filename):
    """Loads plain text article into memory."""
    with open(os.path.join("local", filename), "r") as f:
        return f.readlines()


def get_all_files():
    """Gets list of valid markdown articles."""
    exclude_list = [".DS_Store", ".wh..wh..opq"]
    return [get_file_details(x) for x in os.listdir("local") if x not in exclude_list]


def get_all_tags():
    """Creates sorted container of article filter tags."""
    files = get_all_files()
    tags = defaultdict(int)
    for file in files:
        assert file is not None, f"{files}"
        for t in file.get("tags"):
            tags[t] += 1
    tags = sorted(tags.items(), key=itemgetter(1), reverse=True)
    return tags


def parse_files_and_filters(filters):
    """Loads all articles into memory then filters to subset of articles."""
    files = get_all_files()

    for key, value in filters.items():
        if files:
            if value:
                if key == "tags":
                    files = [x for x in files if value in x[key]]
                else:
                    files = [x for x in files if x[key] == value]

    files = sorted(files, key=itemgetter("date"), reverse=True)

    return files
