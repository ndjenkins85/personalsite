# Copyright © 2025 by Nick Jenkins. All rights reserved

import re
from pathlib import Path


def clear_expansions_for_one_pager(base_template: str) -> str:
    return re.sub(r"{expansive_[^}]+}", "", base_template)


def get_expansive_summary(path) -> str:
    expansive_summary_path = Path("data", path, "expansive_summary.md")
    if expansive_summary_path.exists():
        expansive_summary_data = expansive_summary_path.read_text()
        return expansive_summary_data
    else:
        return f"summary: could not find {path}"


def get_expansive_tiktok(path) -> str:
    expansive_summary_path = Path("data", path, "expansive_tiktok.md")
    if expansive_summary_path.exists():
        expansive_summary_data = expansive_summary_path.read_text()
        return expansive_summary_data
    else:
        return f"TikTok: could not find {path}"


def get_expansive_bcg(path) -> str:
    expansive_summary_path = Path("data", path, "expansive_bcg.md")
    if expansive_summary_path.exists():
        expansive_summary_data = expansive_summary_path.read_text()
        return expansive_summary_data
    else:
        return f"BCG: could not find {path}"


def get_expansive_page_break() -> str:
    return """

<div class="resume-page-break"></div>
<div class="print-only"><h5>Experience continued</h5></div>
"""


def get_expansive_additional() -> str:
    expansive_additional_path = Path("personalsite/resume/expansive_additional.md")
    return expansive_additional_path.read_text()
