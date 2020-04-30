FROM jenkins/jenkins:lts

MAINTAINER hcylus "hercylus@gmail.com"

ENV TIMEZONE=Asia/Shanghai

USER root

RUN echo "${TIMEZONE}" > /etc/timezone

USER jenkins

COPY plugins.txt /usr/share/jenkins/plugins.txt

RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt
