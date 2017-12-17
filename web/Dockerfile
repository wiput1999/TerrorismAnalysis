FROM nginx:mainline-alpine

COPY /web /usr/share/nginx/html

WORKDIR /usr/share/nginx/

RUN chmod 777 -R html

EXPOSE 80