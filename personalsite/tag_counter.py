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

"""Makes visualizations from article tags."""
from collections import defaultdict
from pathlib import Path
from typing import Dict

from personalsite.file_parsing import get_all_files


def analyse_tag_cooccurance() -> Dict[str, int]:
    """Counts co-occurances of tag<->tag."""
    files = get_all_files()
    tag_cooccurance: Dict[str, int] = defaultdict(int)
    for file in files:
        for tag_1 in file.get("tags", []):
            for tag_2 in file.get("tags", []):
                if tag_1 == tag_2:
                    continue

                tag_cooccurance[create_dot_line(tag_1, tag_2)] += 1
                tag_cooccurance[create_dot_line(tag_2, tag_1)] += 1

    return tag_cooccurance


def create_dot_line(tag_a: str, tag_b: str) -> str:
    """Generates line of dot code, with fixes as needed."""
    tag_a = "graphs" if tag_a == "graph" else tag_a
    tag_b = "graphs" if tag_b == "graph" else tag_b
    return f"{tag_a} -> {tag_b}"


def cooccurance_to_dot(tag_cooccurance: Dict[str, int]) -> str:
    """Generates dot friendly relationship text."""
    dot_build: str = ""
    for tags, times in tag_cooccurance.items():
        for i in range(times):
            dot_build += tags + "\n"
    return dot_build


def write_dot(dot_string: str) -> None:
    file = Path("personalsite", "static", "tags.dot")
    file.write_text(dot_string)


write_dot(cooccurance_to_dot(analyse_tag_cooccurance()))
