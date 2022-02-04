#!/bin/bash
<<EOF

   Portfolio Blog \ Generate \ ReadMe

   Generate the README file by running some preprocessing steps

EOF
CURRENT_SCRIPT_DIRECTORY=${CURRENT_SCRIPT_DIRECTORY:-$(dirname $(realpath $0))}
export SHARED_SCRIPTS_PATH=${SHARED_SCRIPTS_PATH:-$(realpath $CURRENT_SCRIPT_DIRECTORY/scripts)}
export CURRENT_SCRIPT_FILENAME=${CURRENT_SCRIPT_FILENAME:-$(basename $0)}
export CURRENT_SCRIPT_FILENAME_BASE=${CURRENT_SCRIPT_FILENAME%.*}
source "$SHARED_SCRIPTS_PATH/shared-functions.sh"
write_header

usage() {
    write_info "generate-readme" "usage - generate-readme"
    write_info "generate-readme" "./generate-readme.sh [-h or -?]"
    exit 1
}

while getopts ':gh?' opt; do
    case $opt in
    g)
        GENERATE_TREE=1
        write_warning "generate-readme" "generating tree before readme documentation"
        ;;
    h | ?)
        usage
        ;;
    :)
        write_error "generate-readme" "-${OPTARG} requires an argument"
        usage
        ;;
    *)
        write_error "generate-readme" "-${OPTARG} argument is not recognised"
        usage
        ;;
    esac
done

write_info "generate-readme" "generating the filesystem tree"
$CURRENT_SCRIPT_DIRECTORY/generate-tree.sh
if write_response "generate-readme" "generate tree documentation"; then
    write_error "generate-readme" "failed to generate tree documentation"
    exit 1
fi