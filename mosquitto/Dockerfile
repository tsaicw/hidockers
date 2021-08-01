FROM alpine:3.14

# Install Mosquitto MQTT broker
RUN apk add --no-cache mosquitto mosquitto-clients

COPY ca_certificates /etc/mosquitto/ca_certificates
COPY certs /etc/mosquitto/certs

RUN chown -R mosquitto.mosquitto /etc/mosquitto/certs/*

EXPOSE 1883
EXPOSE 8883

ENTRYPOINT ["/usr/sbin/mosquitto"]
