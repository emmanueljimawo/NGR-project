# pull official base image
FROM python:3.8-slim-buster

# set work directory
WORKDIR /usr/src/app

RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "vim"]
RUN ["apt-get", "install", "-y", "git"]

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r /usr/src/app/requirements.txt

# copy entrypoint-prod.sh
COPY ./scripts/entrypoint_prod.sh /usr/src/app/scripts/entrypoint_prod.sh

# copy project
COPY . /usr/src/app/

# run entrypoint_prod.sh
ENTRYPOINT ["/usr/src/app/scripts/entrypoint_prod.sh"]

