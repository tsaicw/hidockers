#!/bin/bash

NETOPEER2_PATH=${NETOPEER2_PATH:-/opt/netopeer2}
SYSREPO_REPO_PATH=${NETOPEER2_PATH}/etc/sysrepo
SYSREPO_DATA_PATH=${SYSREPO_REPO_PATH}/data
SYSREPO_YANG_PATH=${SYSREPO_REPO_PATH}/yang

SYSREPOCTL=${NETOPEER2_PATH}/bin/sysrepoctl
SYSREPOCFG=${NETOPEER2_PATH}/bin/sysrepocfg
NETOPEER2_CLI=${NETOPEER2_PATH}/bin/netopeer2-cli
NETOPEER2_SERVER=${NETOPEER2_PATH}/sbin/netopeer2-server
NETOPEER2_SERVER_PIDFILE=${NETOPEER2_PATH}/netopeer2-server.pid

CUSTOM_YANG_PATH=${NETOPEER2_PATH}/share/yang/modules/custom
NETCONF_SSH_PORT=${NETCONF_SSH_PORT:-830}


#
# Functions
#
function job_title { echo -e "\e[32m\n====== ${1} ======\e[39m"; }
function show_info { echo -e "\e[33m${1}\e[39m"; }
function error_info { echo -e "\e[31m${1}\e[39m"; }


#
# ========== ConfD server ==========
#
function install_yang_modules_into_sysrepo {
  job_title "Install the specified YANG modules into sysrepo"

  if [ -d ${CUSTOM_YANG_PATH} ]; then
    YANG_MODULES=$(ls -p ${CUSTOM_YANG_PATH}/*.yang)
    for module in ${YANG_MODULES[@]}; do
      module_name=$(basename ${module} | cut -d. -f1 | cut -d@ -f1)
      if [ $(${SYSREPOCTL} --list | grep ${module_name} | wc -l) -eq 0 ]; then
        show_info "Install ${module_name} module"
        ${SYSREPOCTL} --install ${module}
      else
        revision=$(basename ${module} | cut -d. -f1 | cut -d@ -f2)
        if [ "${revision}" != "$(${SYSREPOCTL} --list | grep ${module_name} | awk '{print $3}')"  ]; then
          show_info "Update ${module_name} module to revision ${revision}"
          ${SYSREPOCTL} --update ${module}
        fi
      fi
    done
  fi
}

function init_sysrepo_data {
  job_title "Initialize data of Sysrepo"
  # TODO: implementation
  return 0
}

function start_netopeer2 {
  job_title "Start Netopeer2 server"
  ${NETOPEER2_SERVER} -p ${NETOPEER2_SERVER_PIDFILE}
  show_info "\nNetopeer2 server is up ......\n"

  trap "kill $(cat ${NETOPEER2_SERVER_PIDFILE})" TERM INT; sleep infinity & wait
}


#
# ========== Container entry point ==========
#
echo -e "\e[32m=============== Startup info ===============\e[39m"
echo -e "\e[33m  Sysrepo Data Path: ${SYSREPO_DATA_PATH}"
echo -e "\e[33m  Sysrepo YANG Path: ${SYSREPO_YANG_PATH}"
echo -e "\e[33m  Custom YANG Modules: ${CUSTOM_YANG_PATH}"
echo -e "\e[33m  Netopeer2 PID File: ${NETOPEER2_SERVER_PIDFILE}"
echo -e "\e[33m  SSH Port: ${NETCONF_SSH_PORT}"
echo -e "\e[32m============================================\e[39m"

if [ "${1}" = "bash" -o "${1}" = "ash" ]; then
  exec "$@"
else
  install_yang_modules_into_sysrepo
  init_sysrepo_data

  if [ "${1}" != "--init-only" ]; then
    start_netopeer2
  fi
fi
