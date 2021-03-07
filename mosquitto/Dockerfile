FROM alpine:3.12
LABEL maintainer="galoistsai@gmail.com"

# Environment variables
ENV MQTT_PORT 1883

# Install Mosquitto MQTT broker
RUN apk add --no-cache mosquitto

EXPOSE $MQTT_PORT
ENTRYPOINT ["/usr/sbin/mosquitto"]
