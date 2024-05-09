#!/bin/sh

if [ -d /home/certs ]
then
  cp -R /home/certs /etc/mosquitto/certs
  find /etc/mosquitto/certs/* ! -name README.md | xargs chown mosquitto.mosquitto
fi

/usr/sbin/mosquitto $@
