# ==========================================================
#   ConfD Server (basic v7.6.x)
#   Note:
#     ConfD build dependencies: ssh-keygen, openssl11
#     ConfD runtime dependencies: openssl11
#     netconf-console dependencies: which, Python3 paramiko
# ==========================================================

ARG DISTRO_VERSION=7.9.2009
FROM centos:${DISTRO_VERSION} as build-confd

# Prerequisites
RUN yum update -y && \
    yum install -y epel-release && \
    yum install -y unzip openssh openssl11 make && \
    ln -s /usr/bin/openssl11 /usr/bin/openssl

ARG CONFD_VERSION=7.6
ARG CONFD_OS=linux
ARG CONFD_ARCH=x86_64
ARG CONFD_PATH=/opt/confd

# Build ConfD basic
ADD artifacts/confd-basic-${CONFD_VERSION}.${CONFD_OS}.${CONFD_ARCH}.zip /root
RUN mkdir -p /root/confd-basic && \
    cd /root/confd-basic && \
    unzip /root/confd-basic-${CONFD_VERSION}.${CONFD_OS}.${CONFD_ARCH}.zip && \
    ./confd-basic-${CONFD_VERSION}.${CONFD_OS}.${CONFD_ARCH}.signed.bin --skip-verification && \
    ./confd-basic-${CONFD_VERSION}.${CONFD_OS}.${CONFD_ARCH}.installer.bin ${CONFD_PATH}

# Remove unnecessary stuffs
RUN cp -R ${CONFD_PATH}/src/confd/build ${CONFD_PATH} && \
    rm -rf ${CONFD_PATH}/{doc,examples.confd,man,src}


FROM centos:${DISTRO_VERSION} as confd

# Prerequisites
RUN yum update -y && \
    yum install -y epel-release && \
    yum install -y which python3-pip openssl11 make xmlstarlet && \
    pip3 install --upgrade pip && \
    pip3 install paramiko && \
    ln -s /usr/bin/openssl11 /usr/bin/openssl &&\
# Clear cache on system
    yum clean all && rm -rf /var/cache/yum/*

ARG CONFD_PATH=/opt/confd

ENV CONFD_PATH=${CONFD_PATH}
WORKDIR ${CONFD_PATH}

COPY --from=build-confd ${CONFD_PATH} ${CONFD_PATH}
