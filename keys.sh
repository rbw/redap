#!/usr/bin/env sh

echo '
     __                __
    / /___ _____  ____/ /___ _____  ________
   / / __ `/ __ \/ __  / __ `/ __ \/ ___/ _ \
  / / /_/ / /_/ / /_/ / /_/ / / / / /__/  __/
 /_/\__,_/ .___/\__,_/\__,_/_/ /_/\___/\___/
        /_/ key management
'

usage() {
    echo "Usage: [ get | add | del ]"
}

wrapped_cmd() {
    context_file=$(dirname $0)/.context
    if [ -f ${context_file} ]; then
        container_id=$(cat ${context_file})
        command=$(docker exec ${container_id} flask auth $1 $2 2>&1);
    else
        command=$(flask auth $1 $2 2>&1);
    fi

    echo "${command}" | sed "s/flask auth //"
}

case $1 in
    get|add|del) wrapped_cmd $1 $2;;
    *) usage ;;
esac

