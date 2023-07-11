# ConfD Container

## Environment
* CentOS 7.9.2009
* ConfD basic 7.6

## Usages
* Build container images
  ```console
  docker image build . -t confd:latest
  docker-compose build confd
  ```
* Run it
  ```console
  docker container run --rm -it confd:latest
  docker-compose run --rm confd
  ```
