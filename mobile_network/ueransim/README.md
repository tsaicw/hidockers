# UERANSIM Container

## Environment
* Alpine 2.17 & Ubuntu 22.04 LTS
* UERANSIM

## Usages
* Build container images (**DISTRO** = alpine | ubuntu)
  ```console
  docker image build -f Dockerfile.<DISTRO> . -t ueransim:<DISTRO>
  docker-compose build <DISTRO>
  ```
* Run it
  ```console
  docker container run --rm -it --cap-add NET_ADMIN --device /dev/net/tun ueransim:<DISTRO>
  docker-compose run --rm <DISTRO>
  ```
