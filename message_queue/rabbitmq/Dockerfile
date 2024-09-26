ARG VERSION=4.0.2
FROM rabbitmq:${VERSION}-management

RUN rabbitmq-plugins enable --offline rabbitmq_mqtt rabbitmq_federation_management rabbitmq_stomp
EXPOSE 1883 61613
