# Netopeer2 Container

## Environment
* Alpine 2.18 & Ubuntu 22.04 LTS
* Netopeer2

## Usages
* Build container images (**DISTRO** = alpine | ubuntu)
  ```console
  docker image build -f Dockerfile.<DISTRO> . -t netopeer2:<DISTRO>
  docker-compose build <DISTRO>
  ```
* Run it
  ```console
  docker container run --rm -it netopeer2:<DISTRO>
  docker-compose run --rm <DISTRO>
  ```
