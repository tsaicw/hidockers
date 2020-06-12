FROM ubuntu:18.04
MAINTAINER Daniel Tsai <galoistsai@gmail.com>

# Environment variables
ENV MQTT_PORT 1883

# Install Mosquitto MQTT broker
RUN apt-get -y update \
 && apt-get -y install mosquitto \
# Remove the APT sources lists
 && rm -rf /var/lib/apt/lists/*

EXPOSE $MQTT_PORT
ENTRYPOINT ["/usr/sbin/mosquitto"]
