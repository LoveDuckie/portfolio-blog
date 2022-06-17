#!/bin/bash
<<EOF

    Portfolio \ Shared Functions Python

    A collection of shared functions that performs Python-based operations.

EOF
[ -n "${SHARED_FUNCTIONS}" ] && return
SHARED_FUNCTIONS=0
CURRENT_SCRIPT_DIRECTORY=${CURRENT_SCRIPT_DIRECTORY:-$(dirname $(realpath $0))}
export SHARED_SCRIPTS_PATH=$(realpath ${SHARED_SCRIPTS_PATH:-$CURRENT_SCRIPT_DIRECTORY})
export REPO_ROOT_PATH=${REPO_ROOT_PATH:-$(realpath $SHARED_SCRIPTS_PATH/../../)}
. "$SHARED_SCRIPTS_PATH/shared-variables.sh"

is_virtualenv_available() {
    if [ -d $REPO_ROOT_PATH/scripts/python/venv ]; then
        return 0
    fi

    return 1
}

create_virtualenv() {
    python -m venv $1    
}

is_python_available() {
    if is_command_available "python"; then
        return 0
    fi

    return 1
}

is_pyenv_available() {
    if is_command_available "pyenv"; then
        return 0
    fi

    return 1
}

is_pyenv_python_version_supported() {
    if ! is_pyenv_installed; then
        return 1
    fi
    PYENV_PYTHON_VERSION=$(pyenv global)
    if [ -z $PYENV_PYTHON_VERSION ]; then
        write_error "shared-functions" "pyenv python version was not discovered."
        return 2
    fi
}

is_pyenv_installed() {
    return [ -d ~/.pyenv ]
}

export -f is_pyenv_available
export -f is_pyenv_python_version_supported
export -f is_python_available
export -f create_virtualenv
export -f is_virtualenv_available
export -f is_pyenv_installed