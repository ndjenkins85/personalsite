# Copyright © 2023 by Nick Jenkins. All rights reserved

"""Nox for python task automation."""

import tempfile
from typing import Any

import nox
from nox.sessions import Session
from nox_poetry import session

locations = "personalsite", "tests", "noxfile.py", "docs/conf.py"
nox.options.sessions = "lint", "tests"
package = "personalsite"


@session(python=["3.12"])
def lint(session: Session) -> None:
    """Runs code quality checks.

    Done in order so that easier to pass tests run first.
    This is in a single command to avoid too much time on environment setup.
    * black - codestyle alignment
    * xdoctest - any code snippets in docstrings are run for correctness
    * mypy - type checking
    * flake8 - code format and consistency checks
    """
    args = session.posargs or locations
    session.install(".[lint]")
    session.run("black", *args)
    session.run("mypy", *args)
    session.run("flake8", *args)


@session(python=["3.12"])
def safety(session: Session) -> None:
    """Runs safety - security checks."""
    session.install(".[dev,tests,lint,docs]")
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--format=requirements.txt",
            "--without-hashes",
            f"--output={requirements.name}",
            external=True,
        )
        session.run("safety", "check", f"--file={requirements.name}", "--full-report")


@session(python=["3.12"])
def tests(session: Session) -> None:
    """Run the test suite, locally, and in CICD process."""
    args = session.posargs or ["-m", "not advanced"]
    session.install(".[tests]")
    session.run("pytest", *args, "-W ignore::DeprecationWarning", external=True)


@session(python=["3.12"])
def docs(session: Session) -> None:
    """Build documentation and static files and push to codebase."""
    session.install(".[docs]")
    session.run("rm", "-rf", "docs/_build", external=True)
    session.run("sphinx-build", "docs", "docs/_build", *session.posargs)
