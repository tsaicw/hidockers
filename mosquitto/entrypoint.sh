#!/bin/sh

if [ -d /etc/mosquitto/certs ]
then
  find /etc/mosquitto/certs/* ! -name README.md | xargs chown mosquitto.mosquitto
fi

/usr/sbin/mosquitto $@
