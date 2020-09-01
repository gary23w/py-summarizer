# pull official base image
FROM python:3.8.3-slim-buster

# set working directory
WORKDIR /usr/src/app

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV ENVIRONMENT prod
ENV TESTING 0

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc \
  && apt-get clean

# install python dependencies
COPY ./Pipfile /usr/src/app/Pipfile 
COPY ./Pipfile.lock /usr/src/app/Pipfile.lock
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile --dev

# add entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# add app
COPY . /usr/src/app

# run entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
#CMD tail -f /dev/null

#
CMD gunicorn --bind 0.0.0.0:5003 app.main:app -k uvicorn.workers.UvicornWorker
