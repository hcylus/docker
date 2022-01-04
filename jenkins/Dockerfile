FROM jenkins/jenkins:lts

MAINTAINER hcylus "hercylus@gmail.com"

ENV TIMEZONE=Asia/Shanghai
ENV JENKINS_UC=http://updates.jenkins.io
# https://mirrors.tuna.tsinghua.edu.cn/jenkins/updates/update-center.json

USER root

RUN echo "${TIMEZONE}" > /etc/timezone

USER jenkins

COPY --chown=jenkins:jenkins plugins.txt /usr/share/jenkins/ref/plugins.txt

RUN jenkins-plugin-cli -f /usr/share/jenkins/ref/plugins.txt --available-updates --output txt >  /usr/share/jenkins/ref/update-plugins.txt \
    && mv /usr/share/jenkins/ref/update-plugins.txt /usr/share/jenkins/ref/plugins.txt && jenkins-plugin-cli --verbose -f /usr/share/jenkins/ref/plugins.txt
