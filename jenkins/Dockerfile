FROM jenkins/jenkins:lts
MAINTAINER hcylus "hercylus@gmail.com"

ENV TIMEZONE=Asia/Shanghai

RUN echo "${TIMEZONE}" > /etc/timezone

COPY plugins.txt /usr/share/jenkins/plugins.txt
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt
