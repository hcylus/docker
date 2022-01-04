FROM node:lts-alpine

LABEL maintainer="hcylus <hercylus@gmail.com>"

ENV TIMEZONE=Asia/Shanghai

RUN apk add tzdata && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
&& echo "${TIMEZONE}" > /etc/timezone

RUN npm install -g pm2 && npm cache clean -f