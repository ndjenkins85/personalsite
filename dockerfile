FROM python:3.6

# Create directory for project
#USER root
RUN mkdir -p /workspace
WORKDIR /workspace

# Add all files to Docker working directory
ADD . /workspace
RUN pip install -r env/requirements_conda.txt --no-cache-dir
RUN pip install -r env/requirements_noconda.txt --no-cache-dir

ENV FLASK_ENV="docker"
ENV PYTHONUNBUFFERED=0
