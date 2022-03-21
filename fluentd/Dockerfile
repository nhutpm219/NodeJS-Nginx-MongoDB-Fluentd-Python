# fluentd/Dockerfile
FROM fluent/fluentd:v1.11-1

USER root

RUN apk add --update --virtual .build-deps \
        sudo build-base ruby-dev \
 && sudo gem install \
        fluent-plugin-mongo \
 && sudo gem sources --clear-all \
 && apk del .build-deps \
 && rm -rf /var/cache/apk/* \
           /home/fluent/.gem/ruby/2.5.0/cache/*.gem

COPY conf/fluent.conf /fluentd/etc/
