FROM ubuntu:18.04
MAINTAINER Daniel Tsai <galoistsai@gmail.com>

# Environment variables
ARG jdkVersion=11

# Install OpenJDK 11
RUN apt-get -y update
RUN apt-get -y install openjdk-${jdkVersion}-jdk

# Update packages and install curl
RUN apt-get -y install curl && apt-get -y upgrade && apt-get -y autoremove

# Remove the APT sources lists
RUN rm -rf /var/lib/apt/lists/*

