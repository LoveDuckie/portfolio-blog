#!/bin/bash
<<EOF

   Portfolio Blog \ Publish \ Blogs

   Publish all blogs that are found under "/blogs/" in the root of the repository.

EOF
CURRENT_SCRIPT_DIRECTORY=${CURRENT_SCRIPT_DIRECTORY:-$(dirname $(realpath $0))}
export SHARED_SCRIPTS_PATH=${SHARED_SCRIPTS_PATH:-$(realpath $CURRENT_SCRIPT_DIRECTORY/scripts)}
export CURRENT_SCRIPT_FILENAME=${CURRENT_SCRIPT_FILENAME:-$(basename $0)}
export CURRENT_SCRIPT_FILENAME_BASE=${CURRENT_SCRIPT_FILENAME%.*}
source "$SHARED_SCRIPTS_PATH/shared-functions.sh"
write_header

is_valid_blog() {
   if [ ! -z $1 ]; then
      write_error "publish" "the blog slug was not specified as the parameter."
      exit 1
   fi
   exit 0
}

usage() {
   exit 0
}

while getopts ':b:h?' opt; do
   case $opt in
        b)
         BLOG_SLUG_NAME=$OPTARG
         write_warning "publish" "publishing \"$BLOG_SLUG_NAME\""
        ;;
        h|?)
            usage
        ;;
        :)
            write_error "publish" "-${OPTARG} requires an argument"
            usage
        ;;
   esac
done