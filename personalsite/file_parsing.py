"""Responsible for loading, validating, and filtering article text."""

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
from pathlib import Path
from typing import Any, Dict, Generator, List, Tuple

import markdown
from flask import Markup


def get_file_details(filename: str) -> Dict[str, Any]:
    """Parses a markdown article into python dictionary.

    Args:
        filename (str): article filename

    Returns:
        Dict[str, Any]: Parsed article elements
    """
    # To debug issues with 'None', remove the try except here to get info on why crashed
    assert len(filename.split(".")) == 2, f"{filename} needs 1x . character (md)"
    details, filetype = filename.split(".")

    assert len(details.split("_")) == 4, f"{filename} needs 3x '_' for date, type, title, tags"
    date, major_type, title, tag_text = details.split("_")

    title_cap = title.replace("-", " ").capitalize()

    tags: List[str] = []
    if tag_text:
        tags = tag_text.split("-")

    year, month, day = date.split("-")

    if month in ["01", "02", "03", "04"]:
        period = f"{year}_early"
    elif month in ["05", "06", "07", "08"]:
        period = f"{year}_mid"
    elif month in ["09", "10", "11", "12"]:
        period = f"{year}_late"
    else:
        period = ""

    url_helper = f"{major_type}/{year}/{month}/{day}/{title}"

    article = open_article(filename)

    teaser = article[0].replace("â€˜", "'").replace("â€™", "'")
    teaser = Markup(markdown.markdown(teaser))

    joined_article = "".join(article).replace("â€˜", "'").replace("â€™", "'")
    joined_article = Markup(markdown.markdown(joined_article))
    joined_article = joined_article.replace("img alt", "img class=img-thumbnail alt")

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
        "article": joined_article,
    }


def open_article(filename: str) -> List[str]:
    """Loads plain text article into memory.

    Args:
        filename (str): article filename

    Returns:
        str: raw article text
    """
    input_path = Path("local", filename)
    with open(input_path, "r") as f:
        return f.readlines()


def get_all_files() -> List[Dict[str, Any]]:
    """Gets list of valid markdown articles.

    Returns:
        List[Dict[str, Any]]: List of parsed articles.
    """
    exclude_list: List[str] = [".DS_Store", ".wh..wh..opq"]
    future_use: Generator[Path, None, None] = Path("local").rglob("*.md")
    future_use
    return [get_file_details(x) for x in os.listdir("local") if x not in exclude_list]


def get_all_tags() -> List[Tuple[str, int]]:
    """Creates sorted container of article filter tags.

    Returns:
        List[Tuple[str, int]]: Returns collection of tags
    """
    files = get_all_files()
    tags: Dict[str, int] = defaultdict(int)
    for file in files:
        for t in file.get("tags", []):
            tags[t] += 1
    new_tags = sorted(tags.items(), key=itemgetter(1), reverse=True)
    return new_tags


def parse_files_and_filters(filters: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Loads all articles into memory then filters to subset of articles.

    Args:
        filters (Dict[str, Any]): Collection of filters.

    Returns:
        List[Dict[str, Any]]: List of articles post-filters
    """
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
