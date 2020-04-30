FROM jenkins/jenkins:lts

MAINTAINER hcylus "hercylus@gmail.com"

ENV TIMEZONE=Asia/Shanghai

USER root

RUN echo "${TIMEZONE}" > /etc/timezone

USER jenkins

RUN ls -l /tmp/
ADD . /tmp/

RUN ls -l /tmp/

#COPY jenkins/plugins.txt /usr/share/jenkins/plugins.txt

#RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt

#COPY plugins.txt /usr/share/jenkins/ref/plugins.txt

#RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt
