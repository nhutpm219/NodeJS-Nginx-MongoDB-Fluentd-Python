# NodeJS-Nginx-MongoDB-Fluentd-Python

Versions:
- Docker version 20.10.13, build a224086
- Docker Compose version v2.2.3
- Ubuntu 18.04


In this lab:
- Nodejs as web app
- Nginx as HTTP basic authentication
- Mongodb is database
- Fluentd as logs collecter
- Python used to trigger cron job and send email


Noted:
- ERROR: for auth Cannot start service auth: failed to initialize logging driver: dial tcp [::1]:24224: connect: connection refused

-> check firewall or port open in your host
