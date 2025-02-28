# Copyright © 2025 by Nick Jenkins. All rights reserved

"""Parse dynamic resume information."""

import re
from pathlib import Path


def clear_expansions_for_one_pager(base_template: str) -> str:
    """Clean out for one pager.

    Args:
        base_template: to be cleaned

    Returns:
        cleaned template
    """
    return re.sub(r"{expansive_[^}]+}", "", base_template)


def get_expansive_summary(path: str) -> str:
    """Pull in expansive summary doc.

    Args:
        path: path to job

    Returns:
        Summary
    """
    expansive_summary_path = Path("data/jobs", path, "expansive_summary.md")
    if expansive_summary_path.exists():
        expansive_summary_data = expansive_summary_path.read_text()
        return expansive_summary_data
    else:
        return f"summary: could not find {path}"


def get_expansive_tiktok(path: str) -> str:
    """Pull in expansive TikTok info doc.

    Args:
        path: path to job

    Returns:
        Summary
    """
    expansive_summary_path = Path("data/jobs", path, "expansive_tiktok.md")
    if expansive_summary_path.exists():
        expansive_summary_data = expansive_summary_path.read_text()
        return expansive_summary_data
    else:
        return f"TikTok: could not find {path}"


def get_expansive_bcg(path: str) -> str:
    """Pull in expansive BCG info doc.

    Args:
        path: path to job

    Returns:
        Summary
    """
    expansive_summary_path = Path("data/jobs", path, "expansive_bcg.md")
    if expansive_summary_path.exists():
        expansive_summary_data = expansive_summary_path.read_text()
        return expansive_summary_data
    else:
        return f"BCG: could not find {path}"


def get_expansive_page_break() -> str:
    """Custom page break logic.

    Returns:
        page break logic
    """
    return """

<div class="resume-page-break"></div>
<div class="print-only"><h5>Experience continued</h5></div>
"""


def get_expansive_additional() -> str:
    """Pull in additional info doc.

    Returns:
        Summary
    """
    expansive_additional_path = Path("personalsite/resume/expansive_additional.md")
    return expansive_additional_path.read_text()
