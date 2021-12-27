#!/bin/bash
<<EOF

   Portfolio Blog \ Publish \ Export Requirements

   Export the virtual environment requirements for the Python script.

EOF
CURRENT_SCRIPT_DIRECTORY=${CURRENT_SCRIPT_DIRECTORY:-$(dirname $(realpath $0))}
export SHARED_SCRIPTS_PATH=${SHARED_SCRIPTS_PATH:-$(realpath $CURRENT_SCRIPT_DIRECTORY/scripts)}
export CURRENT_SCRIPT_FILENAME=${CURRENT_SCRIPT_FILENAME:-$(basename $0)}
export CURRENT_SCRIPT_FILENAME_BASE=${CURRENT_SCRIPT_FILENAME%.*}
source "$SHARED_SCRIPTS_PATH/shared.sh"
write_header

usage() {
   write_info "export-requirements" ""
}

while getopts ':t:h?' opt; do
   case $opt in
   t)
      TARGET_PATH=
      
      ;;
   h | ?)
      usage
      ;;
   :)
      write_error "export-requirements" "-${OPTARG} requires an argument"
      usage
      ;;
   esac
done
