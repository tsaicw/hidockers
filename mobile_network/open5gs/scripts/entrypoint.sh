#!/bin/bash

OPEN5GS_CMD=/usr/local/bin/open5gs

function mongodb_start {
  if [ $(ps aux | grep mongod | grep -v grep | wc -l) -eq 0 ]; then
    /usr/bin/mongod --config /etc/mongod.conf &
    echo -e "\e[92mWait for MongoDB server startup ...\n\e[39m"
    sleep 5
  fi
}

function stop_entrypoint {
  ${OPEN5GS_CMD} stop
  run=false
}

function open5gs_start {
  ${OPEN5GS_CMD} create_tuntap
  ${OPEN5GS_CMD} setup
  ${OPEN5GS_CMD} start
}


#
# ========== Start from here ==========
#
mongodb_start

if [ "${1}" = "bash" ]; then
  exec "$@"
else
  open5gs_start

  trap 'stop_entrypoint' TERM INT
  while ${run}; do sleep 1; done
fi
