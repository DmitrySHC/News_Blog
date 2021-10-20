FROM python:3.9

ENV PYTHONUNBUFFERED 1
RUN mkdir /usr/src/blog

WORKDIR /usr/src/blog

COPY . /usr/src/blog

RUN pip install -r /usr/src/blog/requirements.txt
