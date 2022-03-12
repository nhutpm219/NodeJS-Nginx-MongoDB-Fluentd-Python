FROM nginx:latest
COPY ./index.html /usr/share/nginx/html/index.html

WORKDIR /opt

COPY auth.conf auth.htpasswd launch.sh ./

RUN chmod 0755 ./launch.sh

CMD ["./launch.sh"]
