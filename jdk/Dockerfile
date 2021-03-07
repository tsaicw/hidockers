FROM ubuntu:20.04
LABEL maintainer="galoistsai@gmail.com"

# Build arguments
ARG jdkVersion=11

# Install OpenJDK 11
RUN apt-get -y update \
 && apt-get -y install \
      openjdk-${jdkVersion}-jdk \
      curl \
      vim \
# Remove the APT sources lists
 && rm -rf /var/lib/apt/lists/*

