# DPDK build/run environments Container

## Environment
* Alpine 2.15 & Ubuntu 22.04 LTS
* DPDK 20.11.x

## Usages
* Build container images (**DISTRO** = alpine | ubuntu)
  ```console
  docker image build -f Dockerfile.<DISTRO> . -t dpdk/<buildenv|runenv>:<DPDK_VERSION>-<DISTRO> --target <buildenv|runenv>
  docker-compose build <DISTRO>[-buildenv]
  ```
* Run it
  ```console
  docker container run --rm -it --privileged dpdk/<buildenv|runenv>:<DPDK_VERSION>-<DISTRO>
  docker-compose run --rm <DISTRO>[-buildenv]
  ```
