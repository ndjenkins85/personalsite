FROM python:3.6

# Install requirements
WORKDIR /code
COPY env/requirements_conda.txt /code/requirements_conda.txt
RUN pip install -r requirements_conda.txt --no-cache-dir
COPY env/requirements_noconda.txt /code/requirements_noconda.txt
RUN pip install -r requirements_noconda.txt --no-cache-dir
COPY . /code

ENV FLASK_ENV="docker"
ENV PYTHONUNBUFFERED=0
EXPOSE 5000

CMD gunicorn -b 0.0.0.0:$PORT -k gevent --worker-connections 1000 --timeout 120 personalsite:app
