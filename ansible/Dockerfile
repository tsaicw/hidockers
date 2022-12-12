ARG UBUNTU_VERSION=22.04
FROM ubuntu:${UBUNTU_VERSION}
LABEL maintainer="galoistsai@gmail.com"

ARG ANSIBLE_VERSION=7.1.0

# Install related packages
RUN apt-get update \
    && apt-get install -y apt-transport-https ca-certificates gnupg software-properties-common \
                          curl vim git zip python3-pip \
# Install Ansible & ansible[azure] module
    && pip3 install ansible==${ANSIBLE_VERSION} \
    && pip3 install netaddr boto

# Install Azure CLI
RUN curl -sL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor | tee /etc/apt/trusted.gpg.d/microsoft.gpg > /dev/null \
    && echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/azure-cli.list \
    && apt-get update \
    && apt-get install azure-cli \
# Install Azure CLI extensions
    && az extension add --name interactive \
    && az extension add --name azure-devops \
    # && pip3 install 'ansible[azure]' \
# Remove the APT sources lists
    && rm -rf /var/lib/apt/lists/*

# Install AWS CLI 2.0
RUN curl https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip -o /tmp/awscliv2.zip \
    && unzip -d /tmp /tmp/awscliv2.zip \
    && /tmp/aws/install \ 
    # --install-dir <install-dir> --bin-dir <bind-dir>
# AWSａuto completion
    && echo "\n# AWS auto completion\ncomplete -C '/usr/local/bin/aws_completer' aws" >> /root/.bashrc \
    && rm -rf /tmp/aws /tmp/awscliv2.zip

