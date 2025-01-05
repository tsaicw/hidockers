FROM alpine:3.18

# Install Mosquitto MQTT broker
RUN apk update && apk upgrade && \
    apk add mosquitto mosquitto-clients && \
    rm -rf /var/cache/apk/*

RUN mkdir -p /etc/mosquitto/data && \
    chown mosquitto.mosquitto -R /etc/mosquitto/data

EXPOSE 1883 8883

COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
CMD ["--config-file", "/etc/mosquitto/mosquitto.conf"]
