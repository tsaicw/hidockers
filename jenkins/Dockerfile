ARG JENKINS_VERSION=lts-slim
FROM jenkins/jenkins:$JENKINS_VERSION
LABEL maintainer="galoistsai@gmail.com"

USER root

# Install DockerCE CLI
RUN apt-get update && apt-get install -y apt-transport-https ca-certificates && \
    install -m 0755 -d /etc/apt/keyrings && \
    curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
         $(. /etc/os-release && echo ${VERSION_CODENAME}) stable" \
         | tee /etc/apt/sources.list.d/docker.list > /dev/null && \
    apt-get update && \
    apt-get install -y docker-ce-cli && \
# Remove the APT sources lists
    rm -rf /var/lib/apt/lists/*

# Install alternative oracle JDK 8u261
# ADD artifacts/jdk-8u261-linux-x64.tar.gz /opt/java
# RUN chown -R root.root /opt/java/jdk1.8.0_261

USER jenkins

# Install jenkins plugins
RUN jenkins-plugin-cli --plugins \
        ansible \
        ansicolor \
        blueocean \
        build-timeout \
        cloudbees-disk-usage-simple \
        cloudbees-folder \
        command-launcher \
        configuration-as-code \
        credentials \
        credentials-binding \
        dark-theme \
        docker-commons \
        docker-plugin \
        docker-workflow \
        email-ext \
        git \
        git-parameter \
        github \
        github-branch-source \
        gitlab-plugin \
        gradle \
        htmlpublisher \
        http_request \
        junit \
        ldap \
        mailer \
        matrix-auth \
        metrics \
        # Office-365-Connector \
        pam-auth \
        pipeline-github-lib \
        pipeline-graph-view \
        prometheus \
        publish-over-ssh \
        rebuild \
        s3 \
        slack \
        ssh \
        ssh-slaves \
        terraform \
        timestamper \
        workflow-aggregator \
        ws-cleanup
