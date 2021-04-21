FROM jenkins/jenkins:lts-slim
LABEL maintainer="galoistsai@gmail.com"

USER root

# Install DockerCE CLI
RUN apt-get update && apt-get install -y apt-transport-https ca-certificates \
        vim gnupg software-properties-common
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - > /dev/null 2>&1 \
      && add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable" \
           | tee /etc/apt/sources.list.d/docker.list > /dev/null \
      && apt-get update \
      && apt-get install -y docker-ce-cli \
# Remove the APT sources lists
      && rm -rf /var/lib/apt/lists/*

# Install alternative oracle JDK 8u261
# ADD artifacts/jdk-8u261-linux-x64.tar.gz /opt/java
# RUN chown -R root.root /opt/java/jdk1.8.0_261

USER jenkins
# Install jenkins plugins
RUN jenkins-plugin-cli --plugins blueocean:1.24.6 \
                                 cloudbees-disk-usage-simple:0.10 \
                                 git:4.7.1 \
                                 github-branch-source:2.10.2 \
                                 gitlab-plugin:1.5.20 \
                                 metrics:4.0.2.7 \
                                 Office-365-Connector:4.14.0 \
                                 prometheus:2.0.10 \
                                 slack:2.47
