#!/bin/bash
<<EOF

   Portfolio Blog \ Python \ Setup

   Setup the virtual environment

EOF
CURRENT_SCRIPT_DIRECTORY=${CURRENT_SCRIPT_DIRECTORY:-$(dirname $(realpath $0))}
export SHARED_SCRIPTS_PATH=${SHARED_SCRIPTS_PATH:-$(realpath $CURRENT_SCRIPT_DIRECTORY/scripts)}
export CURRENT_SCRIPT_FILENAME=${CURRENT_SCRIPT_FILENAME:-$(basename $0)}
export CURRENT_SCRIPT_FILENAME_BASE=${CURRENT_SCRIPT_FILENAME%.*}
source "$SHARED_SCRIPTS_PATH/shared-functions.sh"
write_header

while getopts ':t:h?' opt; do
   case $opt in
        t)
            TARGET_PATH=$OPTARG
            write_warning "setup" "target path for project is \"$OPTARG\""
        ;;
        h|?)
            usage
        ;;
        :)
            write_error "setup" "-${OPTARG} requires an argument"
            usage
        ;;
   esac
done