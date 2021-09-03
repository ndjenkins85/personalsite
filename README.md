### Poetry

Ensure you have and installation of Poetry 1.2.0a1 or above, along with poetry-version-plugin.

Make sure you deactivate any existing virtual environments (i.e. conda).

```bash
poetry install
```

You may need to point poetry to the correct python interpreter using the following command.
In another terminal and in conda, run `which python`.
```bash
poetry env use /path/to/python3
```

Enter the poetry shell.

```bash
poetry shell
```

Remove tools not required by poetry, but required for conda
- Delete `setup.py`
- Delete `docs/requirements.txt`
- Edit Conda references in `README.md`

### Conda

*Note*: using conda will mean incompatability with some Nox, Github actions, and library publish functionality. Only the default Nox sessions are included (with light flake8 checks), plus black and docs.

```bash
conda env create -f environment.yml
conda activate my_project
```

Additional conda related setup:

* Setup project details in `setup.py`.
* Remove or update the following Github Actions:
  * coverage
  * release
  * test-pypi
  * tests
* Update project README specify conda instructions

### Docker-compose

Not currently supported, future TODO.

```bash
docker-compose up
```

## 3. Instantiate pre-commit, add log directory, create new git repo

```bash
pre-commit install
git init
git add .
git add logs/.gitkeep --force
git commit -m "initial commit"
git tag 0.1.0
```

Create a repo in github and follow instructions to push (including tags).

Check if the branch name is `main` or `master` - Github Actions are set to use `main`.

## 4. Other setup and cleanup

- Check python and library versions in noxfile and Github actions
- Setup Codecov connection
- Setup pypi and test-pypi secrets, uncomment test-pypi github action
- In Github repo set up dependabot and Github pages
- Change [LICENSE](LICENSE) as required. Use [this guide](https://github.com/Lucas-C/pre-commit-hooks#removing-old-license-and-replacing-it-with-a-new-one) to redo licenses across project

Change name from my_project to new name in:

- project folder name and imports
- `README.md`
- `CONTRIBUTING.md`
- `.flake8`
- `pyproject.toml`
- `docs/conf.py`
- `setup.py`

# My Project

What is it, at a high high level?
Who is the audience or end users? Any requirements?
What are the feature and benefits?

* [Instructions for users](#instructions-for-users)
* [Instructions for developers](#instructions-for-developers)
  * [Dependency and virtual environment management, library development and build with poetry](#dependency-and-virtual-environment-management-library-development-and-build-with-poetry)
  * [Dependency and virtual environment management, library development and build with conda](#dependency-and-virtual-environment-management-library-development-and-build-with-conda)
  * [Code quality, testing, and generating documentation with Nox](#code-quality-testing-and-generating-documentation-with-nox)
  * [Code formatting with Pre-commit](#code-formatting-with-pre-commit)
* [Contributors](#contributors)

## Instructions for users

The following are the quick start instructions for using the project as an end-user.
[Instructions for developers](#instructions-for-developers) follows this section.

Installation (Note, not actually functioning):

```bash
pip install my_project
```

Include an example of running the program with expected outputs.

```bash
python -m my_project.utils -i1 environment.yml -i2 environment.yml -v
...
2021-08-29 14:59:09,489 [DEBUG] Loading main file from environment.yml
2021-08-29 14:59:09,489 [DEBUG] Loading second file from environment.yml
...
  - pytest-cov=2.10.1
  - python=^3.8
  - sphinx=3.2.1
  - sphinx-autodoc-typehints=1.12.0
  - sphinx_rtd_theme=0.4.3
```

Can also be run as a script.

```bash
my_project -i1 environment.yml -i2 environment.yml -v
```

## Instructions for developers

The following are the setup instructions for developers looking to improve this project.
For information on current contributors and guidelines see the [contributors](#contributors) section.
Follow each step here and ensure tests are working.

### Dependency and virtual environment management, library development and build with poetry

Ensure you have and installation of Poetry 1.2.0a1 or above, along with poetry-version-plugin.

Make sure you deactivate any existing virtual environments (i.e. conda).

```bash
poetry install
```

You may need to point poetry to the correct python interpreter using the following command.
In another terminal and in conda, run `which python`.
```bash
poetry env use /path/to/python3
```

Library can be built using

```bash
poetry build
```

### Dependency and virtual environment management, library development and build with conda

Following commands will create the conda environment and setup the library in interactive development mode using setup.py.

```bash
conda env create -f environment.yml
conda activate my_project
pip install -e .
```

Library can be built using

```bash
python setup.py bdist_wheel
```

### Code quality, testing, and generating documentation with Nox

Nox is a python task automation tool similar to Tox, Makefiles or scripts.

The following command can be used to run mypy, lint, and tests.
It is recommended to run these before pushing code, as this is run with Github Actions.
Some checks such as black are run more frequently with [pre-commit](#installing-pre-commit).

```bash
poetry run nox
```

Local Sphinx documentation can be generated with the following command.
Documentation publishing using Github Actions to Github pages is enabled by default.

```bash
poetry run nox -s docs
```

All other task automations commands can be optionally run locally with below command.

```bash
poetry run nox -s black safety pytype typeguard coverage xdoctest autoflake
```

### Code formatting with Pre-commit

On first time use of the repository, pre-commit will need to be installed locally.
You can use the following command to install and run pre-commit over all files.
See .pre-commit-config.yaml for checks in use.
Intention is to have lightweight checks that automatically make code changes.

``` bash
pre-commit run --all-files
```

## Contributors

* [Nick Jenkins](https://www.nickjenkins.com.au) - Data Scientist, API & Web dev, Team lead, Writer

See [CONTRIBUTING.md](CONTRIBUTING.md) in Github repo for specific instructions on contributing to project.

Usage rights governed by [LICENSE](LICENSE)  in Github repo or page footer.


### Conda environment
Create conda environment and install for local running and debugging
``` bash
conda update -n base conda --yes
conda create -n personalsite
conda activate personalsite
conda install -n personalsite --yes --file env/requirements_conda.txt
pip install -r env/requirements_noconda.txt

```

### Local Docker
``` bash
docker build -t bluemania/personalsite .
docker run -p 5000:5000 -e PORT=5000 --rm bluemania/personalsite

```
```bash
docker stop $(docker ps -a -q)
```

### Push Docker

``` bash
heroku login
docker build -t bluemania/personalsite .
heroku container:login
docker tag bluemania/personalsite registry.heroku.com/nickjenkins/web
docker push registry.heroku.com/nickjenkins/web
heroku container:release web -a nickjenkins

```

