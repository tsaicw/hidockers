ARG JENKINS_VERSION=lts-slim
FROM jenkins/jenkins:$JENKINS_VERSION
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
RUN jenkins-plugin-cli --plugins \
        ansible \
        ansicolor \
        blueocean \
        cloudbees-disk-usage-simple \
        configuration-as-code \
        credentials \
        credentials-binding \
        docker-commons \
        docker-plugin \
        docker-workflow \
        git \
        git-parameter \
        github \
        github-branch-source \
        gitlab-plugin \
        htmlpublisher \
        http_request \
        junit \
        metrics \
        Office-365-Connector \
        prometheus \
        publish-over-ssh \
        rebuild \
        s3 \
        slack \
        ssh \
        terraform
