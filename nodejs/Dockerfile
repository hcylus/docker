FROM node:12.16.3-alpine3.11

LABEL maintainer="hcylus <hercylus@gmail.com>"

ENV TIMEZONE=Asia/Shanghai

RUN echo "${TIMEZONE}" > /etc/timezone

# Install pm2
RUN npm install -g pm2
