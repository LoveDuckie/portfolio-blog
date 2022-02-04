#!/bin/bash
<<EOF

   Portfolio Blog \ Generate \ Tree

   Generate the filesystem tree that forms part of the README.md

EOF
CURRENT_SCRIPT_DIRECTORY=${CURRENT_SCRIPT_DIRECTORY:-$(dirname $(realpath $0))}
export SHARED_SCRIPTS_PATH=${SHARED_SCRIPTS_PATH:-$(realpath $CURRENT_SCRIPT_DIRECTORY/shared)}
export CURRENT_SCRIPT_FILENAME=${CURRENT_SCRIPT_FILENAME:-$(basename $0)}
export CURRENT_SCRIPT_FILENAME_BASE=${CURRENT_SCRIPT_FILENAME%.*}
export ROOT_PATH=$(realpath $CURRENT_SCRIPT_DIRECTORY/../../)
source "$SHARED_SCRIPTS_PATH/shared-functions.sh"
write_header

usage() {
    write_info "generate-tree" "usage - generate-tree"
    write_info "generate-tree" "./generate-tree.sh [-h or -?] [-f <target filepath>]"
    exit 1
}

while getopts ':f:h?' opt; do
    case $opt in
    f)
        TARGET_FILEPATH=$OPTARG
        write_warning "generate-tree" "generating tree in \"$TARGET_FILEPATH\""
        ;;
    h | ?)
        usage
        ;;
    :)
        write_error "generate-tree" "\"-${OPTARG}\" requires an argument"
        usage
        ;;
    *)
        write_error "generate-tree" "\"${OPTARG}\" option was not recognised as an argument"
        usage
        ;;
    esac
done

if [ -z "$TARGET_FILEPATH" ]; then
    write_warning "generate-tree" "target filepath was not defined, using \"\" by default."
fi

write_info "generate-tree" "generating tree file"
pushd $ROOT_PATH >/dev/null 2>&1
tree . -L 4 -I "scripts|README|schemas|*log"
popd >/dev/null 2>&1
write_response "generate-tree" "generate tree for documentation"

write_success "generate-tree" "done"
