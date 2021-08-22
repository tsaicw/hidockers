FROM alpine:3.14

# Install Mosquitto MQTT broker
RUN apk add --no-cache mosquitto mosquitto-clients
RUN mkdir -p /etc/mosquitto/data && chown mosquitto.mosquitto -R /etc/mosquitto/data

EXPOSE 1883 8883

COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
CMD ["--config-file", "/etc/mosquitto/mosquitto.conf"]
