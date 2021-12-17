#!/bin/bash
<<EOF

    Portfolio \ Shared Functions

    A collection of shared functions used in various places.

EOF
[ -n "${SHARED_FUNCTIONS}" ] && return
SHARED_FUNCTIONS=0
CURRENT_SCRIPT_DIRECTORY=${CURRENT_SCRIPT_DIRECTORY:-$(dirname $(realpath $0))}
export SHARED_SCRIPTS_PATH=$(realpath ${SHARED_SCRIPTS_PATH:-$CURRENT_SCRIPT_DIRECTORY})
export REPO_ROOT_PATH=${REPO_ROOT_PATH:-$(realpath $SHARED_SCRIPTS_PATH/../../)}
source "$SHARED_SCRIPTS_PATH/shared-variables.sh"

is_docker_installed() {
    if [ -z "$(command -v docker)" ]; then
        return 1
    fi

    return 0
}

is_running_as_root() {
    if [ $(whoami) != 'root' ]; then
        return 0
    else
        return 1
    fi
}

is_command_available() {
    if [ -z "$(command -v $1)" ]; then
        return 1
    else
        return 0
    fi
}

write_header() {
    if [ -z "$HEADER_OUTPUT" ] && [ -e "$SHARED_SCRIPTS_PATH/script-header" ]; then
        echo -e "\e[1;37m$(cat $SHARED_SCRIPTS_PATH/script-header)\e[0m"
    fi

    if [ ! -z "$CURRENT_SCRIPT_FILENAME_BASE" ]; then
        echo ""
        write_info "*** SCRIPT: $(echo \"$CURRENT_SCRIPT_FILENAME_BASE\" | awk '{print toupper($0)}')"
        echo ""
    fi

    export HEADER_OUTPUT=1
}

write_info() {
    MSG=$2
    echo -e "\e[1;36m$1\e[0m \e[1;37m${MSG}\e[0m" 1>&2
}

write_success() {
    MSG=$2
    echo -e "\e[1;32m$1\e[0m \e[1;37m${MSG}\e[0m" 1>&2
}

write_error() {
    MSG=$2
    echo -e "\e[1;31m$1\e[0m \e[1;37m${MSG}\e[0m" 1>&2
}

write_warning() {
    MSG=$2
    echo -e "\e[1;33m$1\e[0m \e[1;37m${MSG}\e[0m" 1>&2
}

write_response() {
    if [ $? -ne 0 ]; then
        write_error "error" "$2"
        return 1
    fi

    write_success "success" "$2"
    return 0
}

is_valid_project() {
    if [ -z "$1" ]; then
        write_error "shared-functions" "the name of the project was not defined."
        return 1
    fi

    if [ ! -d $LOCAL_DOCKER_PATH/projects/$1 ]; then
        write_error "shared-functions" "failed to find \"$1\""
        return 1
    fi

    return 0
}

is_package_installed() {
    if [ -z "$1" ]; then
        write_error "shared-functions" "the name of the ubuntu package was not defined."
        return 1
    fi

    if [[ "$(apt list -a $1)" != "" ]]; then
        return 0
    fi

    write_error "shared-functions" "the package \"$1\" is not installed"
    return 1
}

is_valid_docker_context() {
    if [ -z "$1" ]; then
        write_error "shared-functions" "the docker context was not defined. unable to check."
        return 1
    fi

    local DOCKER_CONTEXT_NAME=${1%%.*}

    write_info "shared-functions" "checking docker context \"${1}\""
    docker context inspect $DOCKER_CONTEXT_NAME >/dev/null 2>&1
    if ! write_response "check docker context \"${1}\""; then
        return 1
    fi

    return 0
}

export -f write_info
export -f write_warning
export -f write_error
export -f write_response
export -f is_valid_docker_context
export -f is_package_installed