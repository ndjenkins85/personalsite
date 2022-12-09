# Copyright © 2023 by Nick Jenkins. All rights reserved

"""Responsible for loading, validating, and filtering article text.

Three main use cases

* Parse all article information into a list of dictionaries
* Parse all articles but return only a filtered subset (could be a single article)
* Parse all articles and get tag information only
"""

# Copyright © 2023 by Nick Jenkins. All rights reserved

import os
from collections import defaultdict
from operator import itemgetter
from pathlib import Path
from typing import Dict, Generator, List, Tuple, Union

import markdown
from flask import Markup


def parse_all_articles() -> List[Dict[str, Union[List, str]]]:
    """Parses all articles in the `local` directory"""
    articles: List[Dict[str, Union[List, str]]] = []
    for article in Path("local").rglob("*.md"):
        _validate_filename(article)
        parsed_article = _parse_article(article)
        articles.append(parsed_article)
    return articles


def parse_all_articles_against_filters(filters: Dict[str, Union[List, str]]) -> List[Dict[str, Union[List, str]]]:
    """Loads all articles into memory then filters to subset of articles.

    Args:
        filters (Dict[str, Union[List, str]]): Filter conditions i.e. tag: [x, y], year: 2022

    Returns:
        List[Dict[str, Union[List, str]]]: List of articles post-filters
    """
    articles = parse_all_articles()
    if not articles:
        return []

    filtered_articles = articles
    for key, value in filters.items():
        if not value:
            continue
        if key == "tags":
            filtered_articles = [article for article in filtered_articles if value in article["tags"]]
        else:
            filtered_articles = [article for article in filtered_articles if article[key] == value]

    filtered_articles = sorted(filtered_articles, key=itemgetter("date"), reverse=True)
    return filtered_articles


def get_all_tags() -> List[Tuple[str, int]]:
    """Parses all articles to get tags sorted by tag counts."""
    articles = parse_all_articles()
    tag_count: Dict[str, int] = defaultdict(int)
    for article in articles:
        for tag in article.get("tags", []):
            tag_count[tag] += 1
    tags = sorted(tag_count.items(), key=itemgetter(1), reverse=True)
    return tags


def _validate_filename(filename: Path) -> None:
    """Checks that a filename conforms to this project's standard for tagging."""
    if len(filename.name.split(".")) != 2:
        err = f"{filename} must contain one full stop only"
        raise ValueError(err)

    if len(filename.stem.split("_")) != 4:
        err = f"{filename} must be separated by three underscores to deliminate date, type, title, tags"
        raise ValueError(err)

    for chunk in filename.stem.split("_"):
        if len(chunk) == 0:
            err = f"{filename} filepart must not be blank"
            raise ValueError(err)

    # This is to ensure title can be referenced directly in URL, and improves local file experience
    if " " in filename.name:
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


def _parse_article(filename: Path) -> Dict[str, Union[List, str]]:
    """Parses a markdown article and metadata into python dictionary.

    Args:
        filename (str): article filename

    Returns:
        Dict[str, Union[List, str]]: Parsed article and metadata
    """
    date, major_type, title, tag_text = filename.stem.split("_")
    year, month, day = date.split("-")
    tags: List[str] = tag_text.split("-")

    url_helper = f"{major_type}/{year}/{month}/{day}/{title}"
    title_cap = title.replace("-", " ").capitalize()

    article_text = filename.open().readlines()
    teaser = _prepare_markdown(article_text[0])
    full_article = _prepare_markdown("".join(article_text))

    return {
        "filename": filename.name,
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
