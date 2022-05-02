#!/bin/bash
<<EOF

    Portfolio \ Shared Functions

    A collection of shared utility functions used for various purposes.

EOF
[ -n "${SHARED_ALL}" ] && return
SHARED_ALL=0
CURRENT_SCRIPT_DIRECTORY=${CURRENT_SCRIPT_DIRECTORY:-$(dirname $(realpath $0))}
export SHARED_SCRIPTS_PATH=$(realpath ${SHARED_SCRIPTS_PATH:-$CURRENT_SCRIPT_DIRECTORY})
export REPO_ROOT_PATH=${REPO_ROOT_PATH:-$(realpath $SHARED_SCRIPTS_PATH/../../)}
source "$SHARED_SCRIPTS_PATH/shared-variables.sh"
source "$SHARED_SCRIPTS_PATH/shared-functions.sh"
source "$SHARED_SCRIPTS_PATH/shared-functions-python.sh"
