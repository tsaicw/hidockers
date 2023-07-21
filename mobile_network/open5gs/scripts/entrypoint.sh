#!/bin/bash

SUPERVISORD_DAEMON=/usr/bin/supervisord
SUPERVISORD_CONFIG=/etc/supervisor/supervisord.conf
SUPERVISORD_PID_FILE=/var/run/supervisord.pid
OPEN5GS_CMD=/usr/local/bin/open5gs

# function mongodb_start {
#   if [ $(ps aux | grep mongod | grep -v grep | wc -l) -eq 0 ]; then
#     /usr/bin/mongod --config /etc/mongod.conf &
#     echo -e "\e[92mWait for MongoDB server startup ...\n\e[39m"
#     sleep 5
#   fi
# }

function entrypoint_terminate {
  ${OPEN5GS_CMD} stop
  if [ -f ${SUPERVISORD_PID_FILE} ]; then
    kill $(cat ${SUPERVISORD_PID_FILE})
  fi
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
${SUPERVISORD_DAEMON} -c ${SUPERVISORD_CONFIG}
# mongodb_start

open5gs_start

trap 'entrypoint_terminate' TERM INT
while ${run}; do sleep 1; done
