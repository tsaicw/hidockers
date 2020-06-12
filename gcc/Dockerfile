FROM ubuntu:18.04
MAINTAINER Daniel Tsai <galoistsai@gmail.com>

# Environment variables

# Install GNU C compiler
RUN apt-get -y update \
 && apt-get -y install \
      build-essential \
      manpages-dev \
      software-properties-common \
      curl \
      vim \
 && add-apt-repository ppa:ubuntu-toolchain-r/test \
 && apt-get -y install \
      gcc-7 \
      g++-7 \
      gcc-8 \
      g++-8 \
      gcc-9 \
      g++-9 \
# Configure multiple GCC versions
 && update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 90 --slave /usr/bin/g++ g++ /usr/bin/g++-9 --slave /usr/bin/gcov gcov /usr/bin/gcov-9 \
 && update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-8 80 --slave /usr/bin/g++ g++ /usr/bin/g++-8 --slave /usr/bin/gcov gcov /usr/bin/gcov-8 \
 && update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 70 --slave /usr/bin/g++ g++ /usr/bin/g++-7 --slave /usr/bin/gcov gcov /usr/bin/gcov-7 \
# Remove the APT sources lists
 && rm -rf /var/lib/apt/lists/*

