FROM ubuntu:22.04

RUN apt-get update -y && apt-get install -y \
      curl wget gnupg2 git vim less

RUN wget -nv -O- https://acli.atlassian.com/gpg/public-key.asc | gpg --dearmor -o /etc/apt/keyrings/acli-archive-keyring.gpg
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/acli-archive-keyring.gpg] https://acli.atlassian.com/linux/deb stable main" | tee /etc/apt/sources.list.d/acli.list > /dev/null

RUN apt-get update -y && apt-get install -y acli
