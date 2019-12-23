import os
from operator import itemgetter
from collections import defaultdict
from flask import Markup
import markdown

def get_file_details(filename):
    """
    To debug issues with 'None', remove the try except here to get info on why crashed
    """

    assert len(filename.split("."))==2, f"{filename} needs 1x . character (md)"
    details, filetype = filename.split(".")

    assert len(details.split("_"))==4, f"{filename} needs 3x '_' for date, type, title, tags"
    date, major_type, title, tags = details.split("_")

    title_cap = title.replace("-"," ").capitalize()

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

    teaser = article[0].replace('â€˜',"'").replace('â€™',"'")
    article = ''.join(article).replace('â€˜',"'").replace('â€™',"'")

    teaser = Markup(markdown.markdown(teaser))        
    article = Markup(markdown.markdown(article))
    article = article.replace("img alt", "img class=img-thumbnail alt")

    return {"filename": filename, "date": date, "major_type": major_type, "title": title, "tags": tags, "year": year, 
            "month": month, "day": day, "period": period, "filename": filename, "filetype": filetype, 
            "title_cap": title_cap, "url_helper": url_helper, 
            "teaser": teaser, "article": article}

def open_article(filename):
    with open(os.path.join("local", filename), 'r') as f:
        article = f.readlines()
    return article


def get_all_files():
    exclude_list = ['.DS_Store']
    return [get_file_details(x) for x in os.listdir("local") if x not in exclude_list]


def get_all_tags():
    files = get_all_files()
    tags = defaultdict(int)
    for file in files:
        assert file is not None, f"{files}"
        for t in file.get("tags"):
            tags[t]+=1
    tags = sorted(tags.items(), key=itemgetter(1), reverse=True)
    return tags


def parse_files_and_filters(filters):
    files = get_all_files()

    for key, value in filters.items():
        if files:
            if value:
                if key=="tags":
                    files = [x for x in files if value in x[key]]
                else:
                    files = [x for x in files if x[key]==value]

    files = sorted(files, key=itemgetter('date'), reverse=True)

    return files

