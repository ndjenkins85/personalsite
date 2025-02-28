# Copyright © 2025 by Nick Jenkins. All rights reserved

import argparse
from pathlib import Path


def get_background_information() -> str:
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
    base_template_path = Path("personalsite/resume/base_template.md")
    base_template = base_template_path.read_text()
    return base_template


def get_job_description(job_name: str) -> str:
    job_description_path = Path("data/jobs", job_name, "job_description.md")
    if not job_description_path.exists():
        raise FileNotFoundError(f"{job_description_path} does not exist")

    job_description_data = job_description_path.read_text()
    return job_description_data


def generate_dynamic_resume_prompt(job_name: str) -> None:
    prompt_dynamic_resume_path = Path("personalsite/resume/prompt_dynamic_resume.md")
    prompt_dynamic_resume_data = prompt_dynamic_resume_path.read_text()

    replacements = {
        "current_resume": get_current_resume(),
        "background_information": get_background_information(),
        "job_description": get_job_description(job_name),
    }

    prompt = prompt_dynamic_resume_data.format(**replacements)
    prompt_path = Path("data/jobs", job_name, "prompt.md")
    if not prompt_path.parent.exists():
        prompt_path.parent.mkdir()
    prompt_path.write_text(prompt)


if __name__ == "__main__":
    # Usage: python -m personalsite.dynamic_resume dummy
    parser = argparse.ArgumentParser(description="Generate a dynamic resume prompt based on a job name.")
    parser.add_argument("job_name", type=str, help="The name of the job to generate a resume prompt for")

    args = parser.parse_args()
    generate_dynamic_resume_prompt(args.job_name)
