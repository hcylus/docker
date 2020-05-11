FROM node:12.16.3-alpine3.11

LABEL maintainer="hcylus <hercylus@gmail.com>"

ENV TIMEZONE=Asia/Shanghai

RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo "${TIMEZONE}" > /etc/timezone

RUN npm install -g pm2
