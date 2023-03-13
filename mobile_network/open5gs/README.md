# Open5GS Container

## Environment
* Ubuntu 22.04 LTS
* Open5GS

## Usages
* Build container images
  ```console
  docker image build . -t open5gs:latest
  docker-compose build
  ```
* Run it
  ```console
  docker container run --rm -it --cap-add NET_ADMIN --device /dev/net/tun open5gs
  docker-compose run --rm open5gs
  ```
