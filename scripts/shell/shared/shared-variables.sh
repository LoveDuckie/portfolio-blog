#!/bin/bash
<<EOF

    Portfolio \ Shared Variables

    A collection of shared variables used in various places.

EOF
[ -n "${SHARED_VARIABLES}" ] && return
SHARED_VARIABLES=0
CURRENT_SCRIPT_DIRECTORY_VARIABLES=${CURRENT_SCRIPT_DIRECTORY_VARIABLES:-$(dirname $(realpath $0))}
export SHARED_SCRIPTS_PATH=$(realpath ${SHARED_SCRIPTS_PATH:-$CURRENT_SCRIPT_DIRECTORY_VARIABLES})
export REPO_ROOT_PATH=${REPO_ROOT_PATH:-$(realpath $SHARED_SCRIPTS_PATH/../../)}
