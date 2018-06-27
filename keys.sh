#!/usr/bin/env sh

echo '
                  __
   ________  ____/ /___ _____
  / ___/ _ \/ __  / __ `/ __ \
 / /  /  __/ /_/ / /_/ / /_/ /
/_/   \___/\__,_/\__,_/ .___/
     key management  /_/

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

