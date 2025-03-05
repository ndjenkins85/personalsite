# Copyright © 2025 by Nick Jenkins. All rights reserved

"""Generate dynamic elements of resume and cover letter (offline)."""

import argparse
import os
from pathlib import Path
from typing import List

import dotenv
import requests


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

    expansive_sections = ["bcg", "tiktok", "summary"]

    for expansive_section in expansive_sections:
        replacements = {
            "expansive_section": expansive_section,
            "current_resume": get_current_resume(),
            "background_information": get_background_information(),
            "job_description": get_job_description(job_name),
        }

        prompt = prompt_dynamic_resume_data.format(**replacements)
        prompt_path = Path("data/jobs", job_name, f"prompt_resume_{expansive_section}.md")
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


def generate_job_relevance(job_name: str) -> None:
    """Generate fully formatted prompt for job relevance test.

    Args:
        job_name: reference for job name
    """
    prompt_job_relevance_path = Path("personalsite/resume/prompt_job_relevance.md")
    prompt_job_relevance_data = prompt_job_relevance_path.read_text()

    replacements = {
        "current_resume": get_current_resume(),
        "job_description": get_job_description(job_name),
    }

    prompt = prompt_job_relevance_data.format(**replacements)
    prompt_path = Path("data/jobs", job_name, "prompt_job_relevance.md")
    if not prompt_path.parent.exists():
        prompt_path.parent.mkdir()
    prompt_path.write_text(prompt)
    print(f"Generated job relevance prompt saved to: {prompt_path}")


def get_jobs() -> List[str]:
    """Parse folder for job names.

    Returns:
        List of job job_names
    """
    job_folders = list(Path("data/jobs").glob("*"))
    job_names = [job_folder.name for job_folder in job_folders if job_folder.is_dir() and job_folder.name != "template"]
    return job_names


def generate_placeholders(job_name: str) -> None:
    templates = [
        "cover_letter.md",
        "expansive_summary.md",
        "expansive_tiktok.md",
        "expansive_bcg.md",
        "rating.md",
    ]
    for template in templates:
        path = Path("data/jobs", job_name, template)
        if not path.exists():
            path.write_text("")


def chat_with_openai(prompt, model="gpt-4o", **kwargs):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"}

    data = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    }

    # Merge additional keyword arguments into the request body
    data.update(kwargs)

    response = requests.post(url, json=data, headers=headers)
    response_json = response.json()

    # Extract the assistant's response
    return response_json.get("choices", [{}])[0].get("message", {}).get("content", "")


def generate_answers(job_name: str) -> None:
    """Generate responses from ChatGPT."""
    base_path = Path("data/jobs", job_name)
    prompts = {
        "prompt_job_relevance.md": "rating.md",
        "prompt_resume_bcg.md": "expansive_bcg.md",
        "prompt_resume_summary.md": "expansive_summary.md",
        "prompt_resume_tiktok.md": "expansive_tiktok.md",
        "prompt_cover.md": "cover_letter.md",
    }
    for prompt_name, answer_name in prompts.items():
        prompt_path = Path(base_path, prompt_name)
        answer_path = Path(base_path, answer_name)

        prompt = prompt_path.read_text()
        answer = answer_path.read_text()
        if len(prompt) > 0 and len(answer) == 0:

            print(f"Prompting from {prompt_path}")
            answer = chat_with_openai(prompt)

            print(f"Saving to {answer_path}")
            answer_path.write_text(answer)


if __name__ == "__main__":
    # Usage: python -m personalsite.dynamic_resume dummy
    parser = argparse.ArgumentParser(description="Generate a dynamic resume prompt based on a job name.")
    parser.add_argument(
        "job_name", type=str, nargs="?", default="", help="The name of the job to generate a resume prompt for"
    )

    args = parser.parse_args()

    dotenv.load_dotenv()

    if not args.job_name:
        jobs = get_jobs()
    else:
        jobs = [args.job_name]

    for job in jobs:
        print(job)
        generate_placeholders(job)
        generate_job_relevance(job)
        generate_dynamic_resume_prompt(job)
        generate_dynamic_cover_letter_prompt(job)
        generate_answers(job)
