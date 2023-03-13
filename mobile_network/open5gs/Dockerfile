ARG UBUNTU_VERSION=22.04
FROM ubuntu:${UBUNTU_VERSION}

ENV IPV4_TUN_SUBNET=10.45.0.0/16
ENV IPV4_TUN_ADDR=10.45.0.1/16
ENV IPV6_TUN_ADDR=cafe::1/64

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y lsb-release curl wget gnupg iproute2 software-properties-common && \
# Mongodb
    wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | apt-key add - && \
    echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu $(lsb_release -cs)/mongodb-org/6.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-6.0.list && \
    apt-get update && \
    apt-get install -y mongodb-org && \
# Open5GS
    add-apt-repository -y ppa:open5gs/latest && \
    apt-get update && \
    apt-get install -y open5gs && \
    rm -rf /var/lib/apt/lists/*

COPY scripts/ /usr/local/bin
