FROM node:0.10

# MAINTAINER golony777 <ccc@example.com>

LABEL maintainer="golony777@example.com" "rating"="Five Stars" "class"="First Class"

USER root

ENV AP /data/app
ENV SCPATH /etc/supervision/conf.d

RUN apt-get -y update

RUN apt-get -y install supervisor
RUN mkdir -p /var/log/supervisor

ADD ./supervisord/conf.d/* $SCPATH

ADD *.js* $AP

WORKDIR $AP

RUN npm install

CMD ["supervisord", "-n"]