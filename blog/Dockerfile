FROM python:3.8
MAINTAINER Zidong
ENV PYTHONUNBUFFERED 1
COPY pip.conf /root/.pip/pip.conf
RUN mkdir -p /var/www/html/blog
WORKDIR /var/www/html/blog
ADD . /var/www/html/blog
RUN pip install Pillow
RUN pip install -r requirements.txt
