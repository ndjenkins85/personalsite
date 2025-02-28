# Copyright © 2025 by Nick Jenkins. All rights reserved

"""Generate dynamic elements of resume and cover letter (offline)."""

import argparse
from pathlib import Path


def get_background_information() -> str:
    """Pull relevant articles and (local) letters.

    Returns:
        Background information
    """
    back_bcg_path = Path(
        "articles/2022-01-09_professional_project-experience-and-impact_career-consulting-interviews.md"
    )
    back_bcg_data = back_bcg_path.read_text()

    back_tt_2023_path = Path("data/background/2023_annual_perf.md")
    back_tt_2023 = back_tt_2023_path.read_text()

    back_tt_2024_path = Path("data/background/2024_annual_perf.md")
    back_tt_2024 = back_tt_2024_path.read_text()

    back_tt_promo_path = Path("data/background/promo_brief_final.md")
    back_tt_promo = back_tt_promo_path.read_text()

    background_info = back_tt_promo + "\n\n" + back_tt_2024 + "\n\n" + back_tt_2023 + "\n\n" + back_bcg_data
    return background_info


def get_current_resume() -> str:
    """Pull current resume.

    Returns:
        Resume information
    """
    base_template_path = Path("personalsite/resume/base_template.md")
    base_template = base_template_path.read_text()
    return base_template


def get_job_description(job_name: str) -> str:
    """Get (local) job description.

    Args:
        job_name: reference for job name

    Raises:
        FileNotFoundError: no job exists

    Returns:
        Job description
    """
    job_description_path = Path("data/jobs", job_name, "job_description.md")
    if not job_description_path.exists():
        raise FileNotFoundError(f"{job_description_path} does not exist")

    job_description_data = job_description_path.read_text()
    return job_description_data


def generate_dynamic_resume_prompt(job_name: str) -> None:
    """Generate fully formatted prompt for resume.

    Args:
        job_name: reference for job name
    """
    prompt_dynamic_resume_path = Path("personalsite/resume/prompt_dynamic_resume.md")
    prompt_dynamic_resume_data = prompt_dynamic_resume_path.read_text()

    replacements = {
        "current_resume": get_current_resume(),
        "background_information": get_background_information(),
        "job_description": get_job_description(job_name),
    }

    prompt = prompt_dynamic_resume_data.format(**replacements)
    prompt_path = Path("data/jobs", job_name, "prompt_resume.md")
    if not prompt_path.parent.exists():
        prompt_path.parent.mkdir()
    prompt_path.write_text(prompt)
    print(f"Generated resume supplemental prompt saved to: {prompt_path}")


def generate_dynamic_cover_letter_prompt(job_name: str) -> None:
    """Generate fully formatted prompt for cover letter.

    Args:
        job_name: reference for job name
    """
    prompt_dynamic_cover_letter_path = Path("personalsite/resume/prompt_dynamic_cover_letter.md")
    prompt_dynamic_cover_letter_data = prompt_dynamic_cover_letter_path.read_text()

    replacements = {
        "current_resume": get_current_resume(),
        "background_information": get_background_information(),
        "job_description": get_job_description(job_name),
    }

    prompt = prompt_dynamic_cover_letter_data.format(**replacements)
    prompt_path = Path("data/jobs", job_name, "prompt_cover.md")
    if not prompt_path.parent.exists():
        prompt_path.parent.mkdir()
    prompt_path.write_text(prompt)
    print(f"Generated cover letter prompt saved to: {prompt_path}")


if __name__ == "__main__":
    # Usage: python -m personalsite.dynamic_resume dummy
    parser = argparse.ArgumentParser(description="Generate a dynamic resume prompt based on a job name.")
    parser.add_argument("job_name", type=str, help="The name of the job to generate a resume prompt for")

    args = parser.parse_args()
    generate_dynamic_resume_prompt(args.job_name)
    generate_dynamic_cover_letter_prompt(args.job_name)
