ARG RUNDECK_IMAGE
FROM ${RUNDECK_IMAGE}

user root

RUN  apt-get update && apt-get install -y apt-transport-https ca-certificates software-properties-common wget git curl jq vim iputils-ping sysstat lsb-release python3-pip

# Install Ansible
RUN pip3 install netaddr boto && \
    pip3 install ansible==2.10.7
    # pip3 install ansible==2.9.27 && pip3 install 'ansible[azure]'

# Install Azure CLI
RUN curl -sL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor | tee /etc/apt/trusted.gpg.d/microsoft.gpg > /dev/null && \
    echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/azure-cli.list && \
    apt-get update && \
    apt-get install -y azure-cli && \
# Remove the APT sources lists
    rm -rf /var/lib/apt/lists/*

# COPY --chown=rundeck:root data/resources.yml /home/rundeck
COPY plugins/. /home/rundeck/libext

user rundeck
