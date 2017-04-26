FROM ubuntu:16.04
MAINTAINER Daniel Tsai <galoistsai@gmail.com>

# Install java 8
ENV sourcesPath /etc/apt/sources.list.d/webupd8team-java.list
RUN echo 'deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main' >> "$sourcesPath" \
    && echo 'deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main' >> "$sourcesPath"
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886
RUN apt-get -y update
RUN /bin/echo debconf shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install oracle-java8-installer oracle-java8-set-default
RUN rm -rf /var/lib/apt/lists/*

