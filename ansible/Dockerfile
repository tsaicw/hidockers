FROM ubuntu:20.04
LABEL maintainer="galoistsai@gmail.com"

# Build arguments
ARG ansibleVersion=2.9.18

ENV DEBIAN_FRONTEND=noninteractive

# Install related packages
RUN apt-get update && apt-get install -y apt-transport-https ca-certificates \
      curl vim gnupg software-properties-common vim git python3-pip \
# Install Ansible & ansible[azure] module
    && pip3 install ansible==${ansibleVersion}} \
    && pip3 install 'ansible[azure]' \
    && pip3 install netaddr

# Install Azure CLI
RUN curl -sL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor | tee /etc/apt/trusted.gpg.d/microsoft.gpg > /dev/null \
    && echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/azure-cli.list \
    && apt-get update \
    && apt-get install azure-cli \
# Remove the APT sources lists
    && rm -rf /var/lib/apt/lists/*

# Install Azure CLI extensions
RUN az extension add --name interactive \
    && az extension add --name azure-devops