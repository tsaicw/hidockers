ARG UBUNTU_VERSION=22.04
FROM ubuntu:${UBUNTU_VERSION}

ENV IPV4_TUN_SUBNET=10.45.0.0/16
ENV IPV4_TUN_ADDR=10.45.0.1/16
ENV IPV6_TUN_ADDR=cafe::1/64

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y lsb-release curl gnupg iproute2 iptables software-properties-common && \
# Mongodb
    curl -fsSL https://www.mongodb.org/static/pgp/server-6.0.asc | gpg --dearmor -o /etc/apt/keyrings/mongodb.gpg && \
    echo "deb [ arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/mongodb.gpg ] https://repo.mongodb.org/apt/ubuntu $(lsb_release -cs)/mongodb-org/6.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-6.0.list && \
    apt-get update && \
    apt-get install -y mongodb-org && \
# Supervisor
    apt-get install -y supervisor && \
# Open5GS
    add-apt-repository -y ppa:open5gs/latest && \
    apt-get update && \
    apt-get install -y open5gs && \
    rm -rf /var/lib/apt/lists/*

# yq: a lightweight and portable command-line YAML, JSON and XML processor
RUN curl -Ls https://github.com/mikefarah/yq/releases/latest/download/yq_linux_amd64 -o /usr/local/bin/yq && chmod +x /usr/local/bin/yq

COPY confs/open5gs.conf /etc/supervisor/conf.d/
COPY scripts/ /usr/local/bin
RUN mv /usr/local/bin/entrypoint.sh /

CMD ["/entrypoint.sh"]
