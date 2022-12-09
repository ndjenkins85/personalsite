"""Responsible for loading, validating, and filtering article text."""

# Copyright © 2023 by Nick Jenkins. All rights reserved

import os
from collections import defaultdict
from operator import itemgetter
from pathlib import Path
from typing import Any, Dict, Generator, List, Tuple

import markdown
from flask import Markup


def _validate_filename(filename: str) -> None:
    """Checks that a filename conforms to this project's standard for tagging."""
    if len(filename.split(".")) != 2:
        err = f"{filename} must contain one full stop only"
        raise ValueError(err)

    if len(filename.split(".")[0].split("_")) != 4:
        err = f"{filename} must be separated by three underscores to deliminate date, type, title, tags"
        raise ValueError(err)

    for chunk in filename.split(".")[0].split("_"):
        if len(chunk) == 0:
            err = f"{filename} filepart must not be blank"
            raise ValueError(err)

    # This is to ensure title can be referenced directly in URL, and improves local file experience
    if " " in filename:
        err = f"{filename} must not contain spaces; use '-' between words and tags"
        raise ValueError(err)


def _prepare_markdown(raw: str) -> str:
    """Takes raw markdown text and prepares html formatting."""
    cleaned = raw
    if len(cleaned) == 0:
        err = "Expected article text, none passed"
        raise ValueError(err)

    cleaned = cleaned.replace("â€˜", "'").replace("â€™", "'")
    cleaned = Markup(markdown.markdown(cleaned))
    cleaned = cleaned.replace("img alt", "img class=img-thumbnail alt")

    return cleaned


def parse_article(filename: str) -> Dict[str, Any]:
    """Parses a markdown article into python dictionary.

    Args:
        filename (str): article filename

    Returns:
        Dict[str, Any]: Parsed article elements
    """
    _validate_filename(filename)
    date, major_type, title, tag_text = filename.split(".")[0].split("_")
    year, month, day = date.split("-")
    tags: List[str] = tag_text.split("-")

    url_helper = f"{major_type}/{year}/{month}/{day}/{title}"
    title_cap = title.replace("-", " ").capitalize()

    article_text = Path("local", filename).open().readlines()

    teaser = _prepare_markdown(article_text[0])
    full_article = _prepare_markdown("".join(article_text))

    return {
        "filename": filename,
        "date": date,
        "year": year,
        "month": month,
        "day": day,
        "major_type": major_type,
        "title": title,
        "tags": tags,
        "title_cap": title_cap,
        "url_helper": url_helper,
        "teaser": teaser,
        "article": full_article,
    }


def parse_all_articles() -> List[Dict[str, Any]]:
    """Gets list of valid markdown articles.

    Returns:
        List[Dict[str, Any]]: List of parsed articles.
    """
    exclude_list: List[str] = [".DS_Store", ".wh..wh..opq"]
    articles = [parse_article(x) for x in os.listdir("local") if x not in exclude_list]
    return articles


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
