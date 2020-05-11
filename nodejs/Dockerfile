FROM node:12.16.3-alpine3.11

LABEL maintainer="hcylus <hercylus@gmail.com>"

ENV TIMEZONE=Asia/Shanghai

RUN apk add tzdata && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
&& echo "${TIMEZONE}" > /etc/timezone && apk del tzdata

RUN npm install -g pm2
