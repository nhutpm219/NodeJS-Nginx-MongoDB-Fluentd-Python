FROM nginx:latest

ENV BASIC_USERNAME=admin
ENV BASIC_PASSWORD=e-bot7
ENV FORWARD_HOST=nodejs
ENV FORWARD_PORT=3000

RUN apt-get update -y \
    && apt-get install -y \
        apache2-utils \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /

COPY nginx.conf /etc/nginx/nginx.conf

COPY launch.sh ./

RUN chmod 0755 ./launch.sh

CMD ["./launch.sh"]
