# Much advice about poetry + docker from https://stackoverflow.com/a/67153715
FROM python:3.12

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

ENV POETRY_VERSION=2.1.1
ENV POETRY_HOME="/opt/poetry"
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV POETRY_NO_INTERACTION=1
ENV PYSETUP_PATH="/opt/pysetup"
ENV VENV_PATH="/opt/pysetup/.venv"
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

EXPOSE 5000

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        # deps for installing poetry
        curl \
        # deps for building python deps
        build-essential

RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./

RUN poetry install --no-root

COPY . /app
WORKDIR /app

CMD gunicorn -b 0.0.0.0:$PORT -k gevent --worker-connections 1000 --timeout 120 personalsite:app
