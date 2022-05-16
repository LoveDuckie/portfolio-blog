#!/bin/bash
<<EOF

   Portfolio Blog \ Publisher \ Export Requirements

   Export the virtual environment requirements for the Python script.

EOF
CURRENT_SCRIPT_DIRECTORY=${CURRENT_SCRIPT_DIRECTORY:-$(dirname $(realpath $0))}
export SHARED_SCRIPTS_PATH=${SHARED_SCRIPTS_PATH:-$(realpath $CURRENT_SCRIPT_DIRECTORY/scripts)}
export CURRENT_SCRIPT_FILENAME=${CURRENT_SCRIPT_FILENAME:-$(basename $0)}
export CURRENT_SCRIPT_FILENAME_BASE=${CURRENT_SCRIPT_FILENAME%.*}
source "$SHARED_SCRIPTS_PATH/shared.sh"
write_header

usage() {
   write_info "export-requirements" "usage - export-requirements"
   exit 1
}

while getopts ':t:h?' opt; do
   case $opt in
   t)
      TARGET_PATH=$OPTARG
      write_info "export-requirements" "using export path \"$TARGET_PATH\""
      ;;
   h | ?)
      usage
      ;;
   :)
      write_error "export-requirements" "\"-${OPTARG}\" requires an argument"
      usage
      ;;
   *)
      write_error "export-requirements" "\"-${OPTARG}\" argument is not required"
      usage
      ;;
   esac
done

write_info "export-requirements" "exporting requirements"

python -m pip freeze > requirements.txt

write_success "export-requirements" "done"