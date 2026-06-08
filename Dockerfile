FROM nginx:alpine

RUN rm -rf /usr/share/nginx/html/*

COPY ./allure-report /usr/share/nginx/html

EXPOSE 80