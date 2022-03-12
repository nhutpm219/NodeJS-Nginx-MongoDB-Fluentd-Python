#!/bin/sh

envsubst < auth.conf > /etc/nginx/conf.d/auth.conf
envsubst < auth.htpasswd > /etc/nginx/auth.htpasswd

htpasswd -c -b /etc/nginx/auth.htpasswd $BASIC_USERNAME $BASIC_PASSWORD

echo basic-auth-pwd
cat /etc/nginx/auth.htpasswd

nginx -g "daemon off;"
