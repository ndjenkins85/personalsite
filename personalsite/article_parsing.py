"""Responsible for loading, validating, and filtering article text."""

# Copyright © 2023 by Nick Jenkins. All rights reserved

import os
from collections import defaultdict
from operator import itemgetter
from pathlib import Path
from typing import Any, Dict, Generator, List, Tuple

import markdown
from flask import Markup


def parse_article(filename: str) -> Dict[str, Any]:
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

    article = Path("local", filename).open().readlines()

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


def parse_all_articles() -> List[Dict[str, Any]]:
    """Gets list of valid markdown articles.

    Returns:
        List[Dict[str, Any]]: List of parsed articles.
    """
    exclude_list: List[str] = [".DS_Store", ".wh..wh..opq"]
    return [parse_article(x) for x in os.listdir("local") if x not in exclude_list]


def get_all_tags() -> List[Tuple[str, int]]:
    """Creates sorted container of article filter tags.

    Returns:
        List[Tuple[str, int]]: Tag counts
    """
    articles = parse_all_articles()
    tag_count: Dict[str, int] = defaultdict(int)
    for article in articles:
        for tag in article.get("tags", []):
            tag_count[tag] += 1
    tags = sorted(tag_count.items(), key=itemgetter(1), reverse=True)
    return tags


def parse_all_articles_against_filters(filters: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Loads all articles into memory then filters to subset of articles.

    Args:
        filters (Dict[str, Any]): Collection of filters.

    Returns:
        List[Dict[str, Any]]: List of articles post-filters
    """
    files = parse_all_articles()

    for key, value in filters.items():
        if files:
            if value:
                if key == "tags":
                    files = [x for x in files if value in x[key]]
                else:
                    files = [x for x in files if x[key] == value]

    files = sorted(files, key=itemgetter("date"), reverse=True)

    return files
