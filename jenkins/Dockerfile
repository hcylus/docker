FROM jenkins/jenkins:lts

MAINTAINER hcylus "hercylus@gmail.com"

ENV TIMEZONE=Asia/Shanghai

USER root

RUN echo "${TIMEZONE}" > /etc/timezone

USER jenkins

RUN ls -l /usr/share/jenkins/

COPY plugins.txt /usr/share/jenkins/plugins.txt

RUN ls -l /usr/share/jenkins/

RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt

#COPY plugins.txt /usr/share/jenkins/ref/plugins.txt

#RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt
